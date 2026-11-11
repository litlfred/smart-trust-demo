---
$schema: folio-memory/v1
id: dir-fictional-countries
label: stable
summary: "Owner directive: the journeys use two fictional countries, Onesa (XXK, home) and Taifafeki (XXR, visited), defined once in scenarios/countries/ for reuse"
createdAt: 2026-11-11
---
Given by the owner on 2026-11-11 (issue #113): instead of Thailand, Malaysia, KSA and Lao PDR, the journeys use the fictional countries Onesa and Taifafeki, each with an ISO 3166-1 user-assigned code, defined once in this repository so other journeys, such as the pilgrimage, reuse them.

Mapping (choice "B", by role): Onesa is the home country (Lao PDR in these journeys, Malaysia in the pilgrimage) and Taifafeki the country visited (Thailand here, KSA in the pilgrimage). Codes: Taifafeki is XXR, the GDHCN DEV test participant whose DSC already signed the J1 DVCs; Onesa is XXK ("another code for the journey home parts... like XXK"), also an onboarded DEV test participant in WorldHealthOrganization/tng-participants-dev. It replaces XXH, which Country B used before. SMART Trust's Participants-DEV value set names the two codes "Onesa" and "Taifafeki" (litlfred/smart-trust).

Places are fictional too: Kesaro (border province of Taifafeki, was Chiang Rai), Lumara (capital of Taifafeki, was Bangkok), Lomaru (capital of Onesa, was Vientiane). The people keep their names. "Malaysia's Hajj Health Card" stays as a real-world policy precedent. Older directives (dir-journeys-demo, dir-vaxlink-story) name the real countries; this one supersedes them on countries and codes.

The WHO guide's own QR Code Generation §12 example, kept as the library's test vector, is a signed payload and keeps its own nationality field.
