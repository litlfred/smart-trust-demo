"""Lay out the overlay's views with room between boxes, and route their lines orthogonally.

Used by build.py, after smart-ra's add_views.py has written the views. Two
steps, each changing only what it says:

1. relayout(): every box of an overlay view gets new <bounds>, worked out from
   the same layout tree add_views.py drew (overlay.VIEWS), or the richer one
   overlay.LAYOUT_TREES gives for the view (which adds "grid" and "space"
   nodes, holding the same boxes in the same groups), but with
   overlay.LAYOUT's gaps instead of add_views.py's 12 px, so a line has room to
   pass between two boxes. Nesting, ids and order are add_views.py's. Every
   size and position is even, so every box's centre is a whole pixel and the
   bendpoints below are exact.

2. route(): every line of an overlay view gets Archi <bendpoint>s for an
   orthogonal route: it leaves its source through a side, runs only
   horizontally and vertically through the gaps, and enters its target
   through a side, never through a box it does not connect, nor through a
   band (a grouping) unless the band holds one of its ends. Lines are routed
   one at a time, shortest first,
   by A* over a grid of lanes 8 px apart through the gaps between boxes, at a
   cost that counts length, each bend, each crossing of a line already
   routed, and (much more) running along one, so lines take lanes of their
   own, and crossing the title in the heading of a box that holds an end costs
   more than crossing it beside the title. Each end leaves or enters at a port
   of its own on the box's side, never under the box's type label at its top
   right, and on a box holding a note (overlay.NOTES) only beside its name,
   or, where the line starts, on its bottom edge. A named line gets one
   more bendpoint, on the line, where its label is clear of every box and
   every other label; cat-harness's renderer draws a label at a line's middle
   point, so the line's first or last point is repeated to make it that.

Archi stores a bendpoint as offsets from the centres of the line's source and
target boxes; both are written, and agree, so Archi and cat-harness's
renderer draw the same route. A line's first and last bendpoints are on its
boxes' sides, where its ends are drawn.

Standard library only; deterministic, so build.py --check compares bytes.
"""

import bisect
import html
import heapq
import re
import uuid

LEAF_W, LEAF_H = 170, 56  # LEAF_H is add_views.py's 55 made even: centres on whole pixels
MARGIN = 10      # how close a line may run to a box it does not connect
LANE = 8         # the spacing of parallel lines
PORT = 12        # the spacing of line ends along a box's side
BEND, CROSS, OVERLAP, SHARED_PORT = 30, 200, 2000, 400
AWAY = 100      # a line's end on a side that does not face the other end
HEADING = 4      # per px of a line run along a heading strip
HEAD = 28        # the heading strip of a box that holds others (add_views.py's)
TYPE_LABEL_W, TYPE_LABEL_H = 116, 18  # cat-harness's renderer: a box's type label, in its top right corner
NOTE_CHARS = 23  # cat-harness's renderer: the characters of a note line in a box 170 px wide (11 px font, 0.56 em a character)


def note_lines(text):
    """How many lines a note of text takes in a box 170 px wide."""
    lines, line = 1, ""
    for wd in text.split():
        nxt = f"{line} {wd}".strip()
        if len(nxt) > NOTE_CHARS and line:
            lines, line = lines + 1, wd
        else:
            line = nxt
    return lines


def note_height(text):
    return 8 + 14 * note_lines(text)
ACROSS_TITLE = 300  # crossing the heading of a box that holds an end, through the middle, where its name is


# --- 1. Layout ---------------------------------------------------------------

def _grid_rows(node):
    """A grid's kids (None is an empty cell) in rows of its column count."""
    cols, kids = node[1], node[2]
    return [kids[i:i + cols] for i in range(0, len(kids), cols)]


def _cell(node, L):
    sizes = [_size(k, L) for k in node[2] if k is not None]
    return (max(w for w, _ in sizes), max(h for _, h in sizes)) if sizes else (LEAF_W, LEAF_H)


def _size(node, L):
    gap, pad, head = L["gap"], L["pad"], L["head"]
    if node[0] == "box":
        # ("box", key) is LEAF_W x LEAF_H; ("box", key, w, h) is a box of its own size.
        return (node[2], node[3]) if len(node) > 2 else (LEAF_W, LEAF_H)
    if node[0] == "space":
        return node[1], node[2]
    if node[0] == "grid":
        # ("grid", cols, kids, indent): cells the size of the largest kid, gap apart, the first indent px in.
        rows, (cw, ch) = _grid_rows(node), _cell(node, L)
        return node[3] + node[1] * cw + (node[1] - 1) * gap, len(rows) * ch + (len(rows) - 1) * gap
    if node[0] == "col":
        sizes = [_size(k, L) for k in node[1]]
        return max(w for w, _ in sizes), sum(h for _, h in sizes) + gap * (len(sizes) - 1)
    kids = node[3] if node[0] == "group" else node[1]
    cols = node[2] if node[0] == "group" else len(kids)
    sizes = [_size(k, L) for k in kids]
    rows = [sizes[i:i + cols] for i in range(0, len(sizes), cols)]
    colw = [max(r[c][0] for r in rows if c < len(r)) for c in range(cols)] if rows else []
    w = sum(colw) + gap * (len(colw) - 1) if rows else LEAF_W
    h = sum(max(s[1] for s in r) for r in rows) + gap * (len(rows) - 1) if rows else 0
    if node[0] == "group":
        return w + 2 * pad, h + head + 2 * pad
    return w, h


def _place(node, x, y, L, out, center):
    """out[key] = (x, y, w, h), relative to the box or group that holds it."""
    gap, pad, head = L["gap"], L["pad"], L["head"]
    if node[0] == "space":
        return
    if node[0] == "grid":
        cw, ch = _cell(node, L)
        for r, row in enumerate(_grid_rows(node)):
            for c, k in enumerate(row):
                if k is not None:
                    _place(k, x + node[3] + c * (cw + gap), y + r * (ch + gap), L, out, center)
        return
    if node[0] in ("col", "row"):
        W, H = _size(node, L)
        c = x if node[0] == "row" else y
        for k in node[1]:
            kw, kh = _size(k, L)
            if node[0] == "col":
                _place(k, x + ((W - kw) // 2 // 2 * 2 if center else 0), c, L, out, center)
                c += kh + gap
            else:
                _place(k, c, y, L, out, center)
                c += kw + gap
        return
    w, h = _size(node, L)
    out[node[1]] = (x, y, w, h)
    if node[0] == "group":
        kids, cols = node[3], node[2]
        sizes = [_size(k, L) for k in kids]
        rows = [sizes[i:i + cols] for i in range(0, len(sizes), cols)]
        colw = [max(r[c][0] for r in rows if c < len(r)) for c in range(cols)]
        cy = head + pad
        for r in range(len(rows)):
            cx = pad
            for c in range(len(rows[r])):
                _place(kids[r * cols + c], cx, cy, L, out, center)
                cx += colw[c] + gap
            cy += max(s[1] for s in rows[r]) + gap


def _absolute(node, out, ox=0, oy=0, acc=None):
    """{key: (x, y)} in the view's coordinates, from out's positions relative to their holders."""
    acc = {} if acc is None else acc
    if node[0] == "space":
        return acc
    if node[0] == "grid":
        for k in node[2]:
            if k is not None:
                _absolute(k, out, ox, oy, acc)
        return acc
    if node[0] in ("col", "row"):
        for k in node[1]:
            _absolute(k, out, ox, oy, acc)
        return acc
    x, y = ox + out[node[1]][0], oy + out[node[1]][1]
    acc[node[1]] = (x, y)
    for k in node[3] if node[0] == "group" else []:
        _absolute(k, out, x, y, acc)
    return acc


def relayout(xml, o):
    """Give every box of each of overlay o's views the bounds of o.LAYOUT; nothing else changes."""
    ids = _ids(o)
    for name, _doc, tree in o.VIEWS:
        tree = getattr(o, "LAYOUT_TREES", {}).get(name, tree)
        L = dict(o.LAYOUT)
        out = {}
        _place(tree, 24, 24, L, out, name in getattr(o, "LAYOUT_CENTERED", ()))
        # o.ALIGN_UNDER[view] = {key: other}: the box key moves sideways to stand under (or over) other.
        for key, other in getattr(o, "ALIGN_UNDER", {}).get(name, {}).items():
            at = _absolute(tree, out)
            x, y, w, h = out[key]
            out[key] = (x + at[other][0] - at[key][0], y, w, h)
        start, end = _view_span(xml, ids("view", name))
        body = xml[start:end]
        for key, (x, y, w, h) in out.items():
            oid = ids("view", name, "obj", key)
            body, n = re.subn(r'(<child xsi:type="archimate:DiagramObject" id="%s"[^>]*>\s*)<bounds [^>]*/>' % oid,
                              lambda m: m.group(1) + f'<bounds x="{x}" y="{y}" width="{w}" height="{h}"/>', body, count=1)
            if n != 1:
                raise SystemExit(f"relayout: {key} is not drawn in {name!r}")
        xml = xml[:start] + body + xml[end:]
    return xml


def _ids(o):
    ns = uuid.uuid5(uuid.NAMESPACE_URL, o.NAMESPACE)
    return lambda *parts: "id-" + uuid.uuid5(ns, "/".join(parts)).hex


def _view_span(xml, vid):
    m = re.search(r'<element xsi:type="archimate:ArchimateDiagramModel" name="[^"]*" id="%s">' % vid, xml)
    if not m:
        raise SystemExit(f"no view {vid}")
    return m.end(), xml.index("\n      </element>", m.end())


# --- 2. Routing --------------------------------------------------------------

def _boxes(body, groupings):
    """{object id: [x, y, w, h, parent, crossable]} in absolute coordinates, and [(conn id, source, target)]."""
    boxes, conns, stack = {}, [], []
    tok = re.compile(r'<child xsi:type="archimate:DiagramObject" id="([^"]+)" archimateElement="([^"]+)"[^>]*>\s*'
                     r'<bounds x="(-?\d+)" y="(-?\d+)" width="(\d+)" height="(\d+)"/>'
                     r'|</child>'
                     r'|<sourceConnection [^>]*id="([^"]+)" source="([^"]+)" target="([^"]+)"')
    for m in tok.finditer(body):
        if m.group(1):
            px, py = (boxes[stack[-1]][0], boxes[stack[-1]][1]) if stack else (0, 0)
            x, y, w, h = (int(v) for v in m.group(3, 4, 5, 6))
            boxes[m.group(1)] = [px + x, py + y, w, h, stack[-1] if stack else None, m.group(2) in groupings]
            stack.append(m.group(1))
        elif m.group(7):
            conns.append(m.group(7, 8, 9))
        else:
            stack.pop()
    return boxes, conns


def _ancestors(boxes, oid):
    out = []
    p = boxes[oid][4]
    while p:
        out.append(p)
        p = boxes[p][4]
    return out


def _ports(lo, length):
    """Port offsets along a side, centre first, then alternately either side."""
    c = lo + length // 2
    out = [c]
    for k in range(1, 40):
        for s in (k, -k):
            v = c + s * PORT
            if lo + 14 <= v <= lo + length - 14:
                out.append(v)
    return out


class _Router:
    def __init__(self, boxes, noted=None):
        self.boxes = boxes
        self.noted = noted or {}  # box: the height of the note at its foot (overlay.NOTES)
        solid = [b for b in boxes.values() if not b[5]]
        xs = {b[0] - MARGIN for b in solid} | {b[0] + b[2] + MARGIN for b in solid}
        ys = {b[1] - MARGIN for b in solid} | {b[1] + b[3] + MARGIN for b in solid}
        x0, x1 = min(b[0] for b in boxes.values()), max(b[0] + b[2] for b in boxes.values())
        y0, y1 = min(b[1] for b in boxes.values()), max(b[1] + b[3] for b in boxes.values())
        xs |= {x0 - 120, x1 + 120}
        ys |= {y0 - 120, y1 + 120}
        self.xs, self.ys = self._lanes(xs), self._lanes(ys)
        # A grouping's heading strip: a line may cross it, but not run along it.
        self.heads = [(b[0], b[1], b[0] + b[2], b[1] + HEAD, HEADING) for b in boxes.values() if b[5]]
        self.used = []  # (horizontal?, fixed, lo, hi)
        self.ports = {}  # (box, side) -> set of offsets used

    def _clear(self, b, oid, side, p, start=False):
        """Whether a line may end at p on that side of box b: never on the type label, nor on a note.

        cat-harness's renderer writes a box's type ("Application Component")
        inside its top right corner, so no line ends on the top edge above it
        or high on the right side beside it, where its arrowhead would touch
        the label. A box holding a note
        (overlay.NOTES) has it at its foot, so a line ends on its sides only
        beside its name, and on its bottom edge only where it starts, with no
        mark there to cover the note.
        """
        x0, y0, x1, y1 = b[0], b[1], b[0] + b[2], b[1] + b[3]
        if side == "top" and p[0] > x1 - TYPE_LABEL_W:
            return False
        if side == "right" and p[1] < y0 + TYPE_LABEL_H:
            return False
        if oid in self.noted:
            return side == "top" or (side == "bottom" and start) or (side in ("left", "right") and y0 + TYPE_LABEL_H <= p[1] <= y1 - 6 - self.noted[oid] - 6)
        return True

    @staticmethod
    def _lanes(edges):
        edges = sorted(edges)
        out = set(edges)
        for a, b in zip(edges, edges[1:]):
            n = 0
            while a + (n + 1) * LANE < b - (n + 1) * LANE and n < 6:
                n += 1
                out |= {a + n * LANE, b - n * LANE}
            out.add((a + b) // 2)
        return sorted(out)

    def route(self, cid, s, t):
        B = self.boxes
        skip = {s, t, *_ancestors(B, s), *_ancestors(B, t)}
        obst = [(b[0] - MARGIN, b[1] - MARGIN, b[0] + b[2] + MARGIN, b[1] + b[3] + MARGIN)
                for k, b in B.items() if k not in skip]  # a band, too, unless it holds an end
        ends = [B[s], B[t]]
        hard = [(b[0], b[1], b[0] + b[2], b[1] + b[3]) for b in ends]
        # A box that holds an end may be crossed, and its heading strip too,
        # straight across but not along it.
        heads = self.heads + [(b[0], b[1], b[0] + b[2], b[1] + HEAD, 40) for b in (B[k] for k in sorted(skip - {s, t})) if not b[5]]
        sb, tb = B[s], B[t]
        sx, sy = _ports(sb[0], sb[2]), _ports(sb[1], sb[3])
        tx, ty = _ports(tb[0], tb[2]), _ports(tb[1], tb[3])
        xs = sorted(set(self.xs) | set(sx) | set(tx) | {sb[0], sb[0] + sb[2], tb[0], tb[0] + tb[2]})
        ys = sorted(set(self.ys) | set(sy) | set(ty) | {sb[1], sb[1] + sb[3], tb[1], tb[1] + tb[3]})
        nx, ny = len(xs), len(ys)
        xi, yi = {v: i for i, v in enumerate(xs)}, {v: i for i, v in enumerate(ys)}
        # The grid, rasterized once per line: blocked nodes, and blocked and
        # costed unit segments (h: (i, j)-(i+1, j); v: (i, j)-(i, j+1)).
        nblock = bytearray(nx * ny)
        hblock, vblock = bytearray(nx * ny), bytearray(nx * ny)
        hcost, vcost = [0.0] * (nx * ny), [0.0] * (nx * ny)
        bl, br = bisect.bisect_left, bisect.bisect_right

        def strict(a, lo, hi):  # indices whose coordinate is strictly inside (lo, hi)
            return range(br(a, lo), bl(a, hi))

        def spans(a, lo, hi):  # unit segments [k, k+1] that lie within [lo, hi]
            return range(bl(a, lo), br(a, hi) - 1)

        for x0, y0, x1, y1 in obst:
            ii, jj = strict(xs, x0, x1), strict(ys, y0, y1)
            for i in ii:
                for j in jj:
                    nblock[i * ny + j] = 1
            for i in spans(xs, x0, x1):
                for j in jj:
                    hblock[i * ny + j] = 1
            for i in ii:
                for j in spans(ys, y0, y1):
                    vblock[i * ny + j] = 1
        for x0, y0, x1, y1 in hard:
            for i in range(bl(xs, x0), br(xs, x1)):
                for j in range(bl(ys, y0), br(ys, y1)):
                    nblock[i * ny + j] = 1
        for x0, y0, x1, y1, w in heads:
            for j in range(bl(ys, y0 - LANE), br(ys, y1 + LANE)):
                for i in range(bl(xs, x0), br(xs, x1) - 1):
                    hcost[i * ny + j] += w * (xs[i + 1] - xs[i])
            for i in range(bl(xs, x0), br(xs, x1)):
                for j in range(bl(ys, y0 - LANE), br(ys, y1 + LANE) - 1):
                    vcost[i * ny + j] += ACROSS_TITLE if w != HEADING and abs(xs[i] - (x0 + x1) / 2) < (x1 - x0) * 0.3 else 15
        for horiz, uf, lo, hi in self.used:
            # a: the axis the used segment runs along; b: the other.
            a, b, par, perp = (xs, ys, hcost, vcost) if horiz else (ys, xs, vcost, hcost)
            idx = (lambda m, k: m * ny + k) if horiz else (lambda m, k: k * ny + m)
            for k in range(br(b, uf - LANE + 2), bl(b, uf + LANE - 2)):  # running along it
                for m in range(max(0, br(a, lo) - 1), min(len(a) - 1, bl(a, hi))):
                    if min(a[m + 1], hi) - max(a[m], lo) > 0:
                        par[idx(m, k)] += OVERLAP
            k = bl(b, uf) - 1  # crossing it: the unit segment [b[k], b[k+1]] with b[k] < uf <= b[k+1]
            if 0 <= k < len(b) - 1:
                for m in strict(a, lo, hi):
                    perp[idx(m, k)] += CROSS

        # Ports: (x, y, direction) on each end box's sides; direction outward for the source, inward for the target.
        def side_ports(b, px, py, out, oid):
            x0, y0, x1, y1 = b[0], b[1], b[0] + b[2], b[1] + b[3]
            res = []
            for x in px:
                res += [((x, y0), (0, -1), "top", x - px[0]), ((x, y1), (0, 1), "bottom", x - px[0])]
            for y in py:
                res += [((x0, y), (-1, 0), "left", y - py[0]), ((x1, y), (1, 0), "right", y - py[0])]
            return [(p, d if out else (-d[0], -d[1]), side, off) for p, d, side, off in res if self._clear(b, oid, side, p, out)]

        # A line leaves and enters by the sides that face the other end: by
        # top or bottom when the other box is more above or below than beside.
        (scx, scy), (tcx, tcy) = (sb[0] + sb[2] / 2, sb[1] + sb[3] / 2), (tb[0] + tb[2] / 2, tb[1] + tb[3] / 2)
        dx, dy = tcx - scx, tcy - scy

        def facing(side, sign):
            want = ("bottom" if dy * sign > 0 else "top") if abs(dy) >= abs(dx) else ("right" if dx * sign > 0 else "left")
            return side == want

        def port_cost(box, side, off):
            return (abs(off) * 0.3 + (0 if facing(side, 1 if box == s else -1) else AWAY)
                    + (SHARED_PORT if off in self.ports.get((box, side), ()) else 0))

        goals = {}
        for (gx, gy), d, side, off in side_ports(tb, tx, ty, False, t):
            goals[xi[gx] * ny + yi[gy]] = (d, side, off)
        tx0, ty0, tx1, ty1 = tb[0], tb[1], tb[0] + tb[2], tb[1] + tb[3]

        def h(x, y):
            return max(0, tx0 - x, x - tx1) + max(0, ty0 - y, y - ty1)

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))  # d ^ 1 is d reversed
        heap, best, came, n = [], {}, {}, 0
        for p, d, side, off in side_ports(sb, sx, sy, True, s):
            # Step out of the box to the first grid line beyond it.
            i, j = xi[p[0]] + d[0], yi[p[1]] + d[1]
            if not (0 <= i < nx and 0 <= j < ny) or nblock[i * ny + j]:
                continue
            g = port_cost(s, side, off) + abs(xs[i] - p[0]) + abs(ys[j] - p[1])
            st = (i * ny + j, DIRS.index(d))
            if g < best.get(st, 1e18):
                best[st] = g
                came[st] = (p, side, off)
                n += 1
                heapq.heappush(heap, (g + h(xs[i], ys[j]), n, g, st))
        found = None
        while heap:
            f, _n, g, st = heapq.heappop(heap)
            if g > best.get(st, 1e18):
                continue
            if found and f >= found[0]:
                break
            k, di = st
            i, j = divmod(k, ny)
            for nd in range(4):
                if nd == di ^ 1:
                    continue
                dx, dy = DIRS[nd]
                ni, nj = i + dx, j + dy
                if not (0 <= ni < nx and 0 <= nj < ny):
                    continue
                if dx:
                    sk = min(i, ni) * ny + j
                    if hblock[sk]:
                        continue
                    cost = xs[max(i, ni)] - xs[min(i, ni)] + hcost[sk]
                else:
                    sk = i * ny + min(j, nj)
                    if vblock[sk]:
                        continue
                    cost = ys[max(j, nj)] - ys[min(j, nj)] + vcost[sk]
                if nd != di:
                    cost += BEND
                nk = ni * ny + nj
                if nk in goals and goals[nk][0] == DIRS[nd]:
                    _gd, side, off = goals[nk]
                    total = g + cost + port_cost(t, side, off)
                    if not found or total < found[0]:
                        found = (total, st, (xs[ni], ys[nj]), side, off)
                    continue
                if nblock[nk]:
                    continue
                ns = (nk, nd)
                ng = g + cost
                if ng < best.get(ns, 1e18):
                    best[ns] = ng
                    came[ns] = st
                    n += 1
                    heapq.heappush(heap, (ng + h(xs[ni], ys[nj]), n, ng, ns))
        if not found:
            raise SystemExit(f"route: no orthogonal route for connection {cid}")
        _total, st, goal, tside, toff = found
        pts = [goal]
        while True:
            prev = came[st]
            i, j = divmod(st[0], ny)
            pts.append((xs[i], ys[j]))
            if len(prev) == 3:  # a port
                pts.append(prev[0])
                _p, sside, soff = prev
                break
            st = prev
        pts.reverse()
        self.ports.setdefault((s, sside), set()).add(soff)
        self.ports.setdefault((t, tside), set()).add(toff)
        # Keep the corners only.
        out = [pts[0]]
        for a, b in zip(pts[1:], pts[2:]):
            p = out[-1]
            if not ((p[0] == a[0] == b[0]) or (p[1] == a[1] == b[1])):
                out.append(a)
        out.append(pts[-1])
        for a, b in zip(out, out[1:]):
            if a[1] == b[1]:
                self.used.append((True, a[1], min(a[0], b[0]), max(a[0], b[0])))
            else:
                self.used.append((False, a[0], min(a[1], b[1]), max(a[1], b[1])))
        return out


LABEL_CHAR, LABEL_H = 5, 12  # cat-harness's renderer: a 9 px label, its baseline 3 px above its point


def _label_rect(x, y, text):
    w = len(text) * LABEL_CHAR + 6
    return (x - w / 2, y - 3 - LABEL_H + 2, x + w / 2, y - 1)


def _with_label(pts, text, solid, placed):
    """pts with one more bendpoint, on the line, where its label is clear of every box and every label placed so far.

    cat-harness's renderer draws a line's label at its middle point, so the
    point is made the middle one by repeating the line's first or last point.
    The rectangle taken is added to placed.
    """
    segs = sorted(range(len(pts) - 1), key=lambda k: (-(abs(pts[k + 1][0] - pts[k][0]) + abs(pts[k + 1][1] - pts[k][1])), k))
    hit = lambda a, b: a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
    choice = None
    for k in segs:
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        for f in (0.5, 0.35, 0.65, 0.2, 0.8):
            x, y = round(x0 + (x1 - x0) * f), round(y0 + (y1 - y0) * f)
            rect = _label_rect(x, y, text)
            if not any(hit(rect, b) for b in solid) and not any(hit(rect, b) for b in placed):
                choice = (k, (x, y), rect)
                break
        if choice:
            break
    if not choice:  # nowhere clear: the middle of the longest segment
        k = segs[0]
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        x, y = round((x0 + x1) / 2), round((y0 + y1) / 2)
        choice = (k, (x, y), _label_rect(x, y, text))
    k, p, rect = choice
    placed.append(rect)
    bends = pts[:k + 1] + [p] + pts[k + 1:]
    i, n = k + 2, len(bends) + 2  # p's index among the points drawn: the clipped start, the bends, the clipped end
    if 2 * i < n - 1:
        bends = [bends[0]] * (n - 1 - 2 * i) + bends
    elif 2 * i > n - 1:
        bends = bends + [bends[-1]] * (2 * i - n + 1)
    return bends


def route(xml, o):
    """Write orthogonal bendpoints for every line of each of overlay o's views."""
    ids = _ids(o)
    groupings = {ids("element", k) for k, e in o.ELEMENTS.items() if e[0] == "Grouping"} | \
                {o.EXISTING[k] for k in o.RA_GROUPINGS}
    for name, _doc, _tree in o.VIEWS:
        start, end = _view_span(xml, ids("view", name))
        body = xml[start:end]
        boxes, conns = _boxes(body, groupings)
        noted = {ids("view", name, "obj", k): note_height(t) for k, t in getattr(o, "NOTES", {}).get(name, {}).items()}
        r = _Router(boxes, noted)

        def centre(b):
            return b[0] + b[2] // 2, b[1] + b[3] // 2

        def dist(c):
            (ax, ay), (bx, by) = centre(boxes[c[1]]), centre(boxes[c[2]])
            return abs(ax - bx) + abs(ay - by)

        todo = [c for c in conns if c[1] not in _ancestors(boxes, c[2]) and c[2] not in _ancestors(boxes, c[1])]
        # Shortest first: the many short lines straight down take their lanes,
        # and the few long ones (where the countries meet) go round them
        # rather than across them all.
        rel = {m.group(1): m.group(2) for m in re.finditer(r'<sourceConnection [^>]*id="([^"]+)"[^>]*archimateRelationship="([^"]+)"', body)}
        order = sorted(todo, key=lambda c: (dist(c), c[0]))
        routes = {c[0]: r.route(*c) for c in order}
        named = dict(re.findall(r'<element xsi:type="archimate:\w+Relationship" id="([^"]+)"[^>]*? name="([^"]*)"', xml))
        solid = [(b[0], b[1], b[0] + b[2], b[1] + b[3]) for b in boxes.values() if not b[5]]
        placed = []
        for c in order:
            label = named.get(rel.get(c[0]))
            if label:
                routes[c[0]] = _with_label(routes[c[0]], html.unescape(label), solid, placed)
        for cid, s, t in conns:
            if cid not in routes:
                continue
            (scx, scy), (tcx, tcy) = centre(boxes[s]), centre(boxes[t])
            bends = "".join(
                "\n" + " " * 12 + "<bendpoint" + "".join(f' {k}="{v}"' for k, v in
                                                     (("startX", x - scx), ("startY", y - scy), ("endX", x - tcx), ("endY", y - tcy)) if v)
                + "/>" for x, y in routes[cid])
            body, n = re.subn(r'(\n( *)<sourceConnection [^>]*id="%s"[^>]*?)/>' % cid,
                              lambda m: m.group(1) + ">" + bends.replace("\n" + " " * 12, "\n" + m.group(2) + "  ") + "\n" + m.group(2) + "</sourceConnection>",
                              body, count=1)
            if n != 1:
                raise SystemExit(f"route: connection {cid} not found in {name!r}")
        xml = xml[:start] + body + xml[end:]
    return xml
