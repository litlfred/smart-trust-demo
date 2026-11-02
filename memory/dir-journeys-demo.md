---
$schema: folio-memory/v1
id: dir-journeys-demo
label: stable
summary: "Owner directive: the demonstrator's four user journeys and their setting (cast and countries superseded by dir-vaxlink-story, 2026-11-02)"
createdAt: 2026-10-23
---
Given by the owner (brief of 2026-10-23): J1 cross-border birth and initial vaccination (mother delivers abroad in Asia; birth doses; clinic issues a signed paper DVC with a QR code); J2 return home, CHW discovery and referral (offline QR read, clinic referral); J3 clinic verification and schedule generation (cryptographic validation of the foreign DVC, import into the domestic EHR, schedule rules); J4 outbound family travel, "One Family, One Phone" (national portal issues IPS and DVCs to a shared family phone as passcode-protected VHL QR codes for point-of-care fetch).

J1 reuses the WHO SMART Trust guide's QR Code Generation section 12 example unchanged: Lao newborn Chanthala SOUVANNALATH, guardian Mali SOUVANNALATH, Hep B and BCG birth doses given by Dr Pimchanok WATTANA, two DVCs issued by GDHCN DEV participant XXR, which verify against the live DEV trust list.

Owner's answers of 2026-10-23: there are two countries, and the country where the child was born is not the country where the parents reside ("the country where the child was born != the country the child's parents reside"). Country A, the birth country, is XXR, the issuer of the J1 DVCs. Country B, the country of residence ("home", where J2 to J4 happen), is a fictional GDHCN DEV participant, written XXH here. The family are Lao nationals resident in Country B; nationality LAO is only a signed field of the certificate, not a third country in the journeys ("Story: Lao family, home fictional"). J1 shows the guide's two signed QRs, Hep B and BCG ("Hep B + BCG"); the birth-dose OPV the brief mentions appears in J3 as a dose the schedule finds due, not as a third certificate.
