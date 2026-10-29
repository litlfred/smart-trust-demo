// Example resources for the journeys J2 to J4.1: the fictional people and
// places they share. Every person here is fictional (AGENTS.md); Chanthala and
// Mali are the WHO SMART Trust guide's QR Code Generation section 12 example.
// J1's DVC payloads wait for a smart-trust-phw package whose DVCMinPreQual
// matches the signed certificates (bean smart-trust-demo-ig01). Dates after
// the birth (2026-10-21) are illustrative: the journeys do not fix them.

Alias: $cvx = http://hl7.org/fhir/sid/cvx
Alias: $loinc = http://loinc.org
Alias: $sct = http://snomed.info/sct
Alias: $v3-RoleCode = http://terminology.hl7.org/CodeSystem/v3-RoleCode

Instance: TrustDemoChanthala
InstanceOf: Patient
Title: "Chanthala SOUVANNALATH (newborn)"
Description: "The subject of every journey, as registered in Country B (XXH) by the CHW in J2. Born 2026-10-21 in Country A (XXR); a Lao national resident in Country B. Fictional."
Usage: #example
* name.family = "SOUVANNALATH"
* name.given = "Chanthala"
* gender = #female
* birthDate = "2026-10-21"
* contact.relationship = $v3-RoleCode#MTH "mother"
* contact.name.family = "SOUVANNALATH"
* contact.name.given = "Mali"

Instance: TrustDemoMali
InstanceOf: RelatedPerson
Title: "Mali SOUVANNALATH (mother)"
Description: "Chanthala's mother and guardian: the Holder of the paper DVCs (J1 to J3) and of the family phone's VHLs (J4). Fictional."
Usage: #example
* patient = Reference(TrustDemoChanthala)
* relationship = $v3-RoleCode#MTH "mother"
* name.family = "SOUVANNALATH"
* name.given = "Mali"

Instance: TrustDemoSitaRai
InstanceOf: Practitioner
Title: "Sita RAI (community health worker, Country B)"
Description: "The CHW who finds Chanthala missing from the household register in J2. Fictional."
Usage: #example
* name.family = "RAI"
* name.given = "Sita"

Instance: TrustDemoTomasAlves
InstanceOf: Practitioner
Title: "Tomas ALVES (nurse, home clinic, Country B)"
Description: "The immunization nurse who verifies the DVCs and gives the birth-dose OPV in J3. Fictional."
Usage: #example
* name.family = "ALVES"
* name.given = "Tomas"

Instance: TrustDemoAnaMoreira
InstanceOf: Practitioner
Title: "Dr Ana MOREIRA (clinician abroad)"
Description: "The emergency-room physician who reads Chanthala's records through the VHL in J4.1. Fictional."
Usage: #example
* name.family = "MOREIRA"
* name.given = "Ana"

Instance: TrustDemoHomeClinic
InstanceOf: Organization
Title: "District clinic, Country B"
Description: "The home district clinic of J3, in Country B (XXH, a fictional GDHCN DEV participant)."
Usage: #example
* name = "District clinic, Country B (fictional)"

Instance: TrustDemoHomeClinicEhr
InstanceOf: Device
Title: "Home clinic EHR, Country B"
Description: "The clinic's record system that verifies the DVCs offline against its cached trust list and imports them (J3)."
Usage: #example
* displayName = "Home clinic EHR, Country B"
* owner = Reference(TrustDemoHomeClinic)

Instance: TrustDemoPocReceiver
InstanceOf: Device
Title: "Point-of-care hospital system abroad"
Description: "The hospital system abroad that verifies the VHL's HCERT, fetches the manifest by ITI-YY5 and decrypts the records (J4.1): a VHL Receiver."
Usage: #example
* displayName = "Point-of-care hospital system abroad"
