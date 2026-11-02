// The people, places and systems the journey examples share. The story is the
// VaxLink workshop walkthrough's (fredhersch/vaxlink): Somsack SENGMANY, a Lao
// baby born in Thailand, followed over his first year. Every person here is
// fictional (AGENTS.md). Country A, the birth country, is Thailand, played on
// the GDHCN DEV network by test participant XXR; Country B, home, is Lao PDR,
// played by the fictional participant XXH. Neither is a real ministry's key.

Alias: $cvx = http://hl7.org/fhir/sid/cvx
Alias: $loinc = http://loinc.org
Alias: $sct = http://snomed.info/sct
Alias: $v3-RoleCode = http://terminology.hl7.org/CodeSystem/v3-RoleCode
Alias: $LaoTmpId = http://smart.who.int/trust-demo/sid/lao-temporary-id
Alias: $HouseholdId = http://smart.who.int/trust-demo/sid/lao-household-id

Instance: TrustDemoSomsack
InstanceOf: TrustDemoLaoPatient
Title: "Somsack SENGMANY (newborn)"
Description: "The subject of every journey, as the CHW registers him in Lao PDR (Country B) in J2: born 2025-10-28 at Chiang Rai Provincial Hospital, Thailand (Country A), with no Thai identity number. Until civil registration catches up he has a temporary id. Fictional."
Usage: #example
* identifier[temporaryId].system = $LaoTmpId
* identifier[temporaryId].value = "LAO-TMP-2025-00918"
* active = true
* name.use = #official
* name.family = "SENGMANY"
* name.given = "Somsack"
* gender = #male
* birthDate = "2025-10-28"
* contact[+].relationship = $v3-RoleCode#MTH "mother"
* contact[=].name.family = "SENGMANY"
* contact[=].name.given = "Khamla"
* contact[+].relationship = $v3-RoleCode#FTH "father"
* contact[=].name.family = "SENGMANY"
* contact[=].name.given = "Bounmy"

Instance: TrustDemoKhamla
InstanceOf: RelatedPerson
Title: "Khamla SENGMANY (mother)"
Description: "Somsack's mother, 26: the Holder of the two paper DVCs from J1 to J3. Fictional."
Usage: #example
* patient = Reference(TrustDemoSomsack)
* relationship = $v3-RoleCode#MTH "mother"
* name.family = "SENGMANY"
* name.given = "Khamla"
* gender = #female

Instance: TrustDemoBounmy
InstanceOf: RelatedPerson
Title: "Bounmy SENGMANY (father, head of household)"
Description: "Somsack's father, 29, head of the household: he holds the family's one shared phone and is the VHL Holder in J4. Fictional."
Usage: #example
* patient = Reference(TrustDemoSomsack)
* relationship = $v3-RoleCode#FTH "father"
* name.family = "SENGMANY"
* name.given = "Bounmy"
* gender = #male

Instance: TrustDemoAnan
InstanceOf: Practitioner
Title: "Dr Anan (clinician, Chiang Rai, Thailand)"
Description: "Gives Somsack's birth doses and prints the DVCs (J1), and reads his record through the VHL a year later (J4.1). Fictional."
Usage: #example
* name.text = "Dr Anan"
* name.given = "Anan"
* name.prefix = "Dr"

Instance: TrustDemoVilay
InstanceOf: Practitioner
Title: "Vilay (community health worker, Village 04, Lao PDR)"
Description: "The CHW who finds Somsack missing from the household roster in J2. Fictional."
Usage: #example
* name.text = "Vilay"
* name.given = "Vilay"

Instance: TrustDemoChanthasone
InstanceOf: Practitioner
Title: "Nurse Chanthasone (Vientiane District Health Center)"
Description: "The nurse who verifies the DVCs and fits the Thai doses to the Lao schedule in J3. Fictional."
Usage: #example
* name.text = "Nurse Chanthasone"
* name.given = "Chanthasone"

Instance: TrustDemoChiangRaiHospital
InstanceOf: Organization
Title: "Chiang Rai Provincial Hospital, Thailand (Country A)"
Description: "The birth hospital of J1. Its DVCs are signed with the DSC of GDHCN DEV test participant XXR, which plays Thailand in the demonstrator."
Usage: #example
* name = "Chiang Rai Provincial Hospital (demonstrator)"
* contact.address.country = "TH"

Instance: TrustDemoVientianeDhc
InstanceOf: Organization
Title: "Vientiane District Health Center, Lao PDR (Country B)"
Description: "The district health center of J3 and of Somsack's later Lao doses."
Usage: #example
* name = "Vientiane District Health Center (demonstrator)"
* contact.address.country = "LA"

Instance: TrustDemoLaoPortalOrg
InstanceOf: Organization
Title: "Lao PDR national health portal (Country B, XXH)"
Description: "The national service that hosts the family's records, issues their VHLs (J4.0) and logs every access (J4.1). On the GDHCN DEV network it is the fictional participant XXH."
Usage: #example
* name = "Lao PDR national health portal (demonstrator, GDHCN DEV participant XXH)"
* contact.address.country = "LA"

Instance: TrustDemoChiangRaiClinic
InstanceOf: Organization
Title: "Chiang Rai primary care clinic, Thailand (J4.1)"
Description: "Where Dr Anan sees Somsack a year after his birth, back in Country A."
Usage: #example
* name = "Chiang Rai primary care clinic (demonstrator)"
* contact.address.country = "TH"

Instance: TrustDemoChwApp
InstanceOf: Device
Title: "CHW app (OHS, community configuration), Lao PDR"
Description: "The offline app on Vilay's phone (J2): household registration, triage read of foreign DVCs (STT-VER-011), referral."
Usage: #example
* displayName = "CHW app, Village 04 (offline)"

Instance: TrustDemoDhcEhr
InstanceOf: Device
Title: "District health center EHR (OHS, facility configuration), Lao PDR"
Description: "The clinic tablet's record system that verifies the DVCs offline against its cached GDHCN trust list, imports them and evaluates the schedule (J3)."
Usage: #example
* displayName = "Vientiane District Health Center EHR"
* owner = Reference(TrustDemoVientianeDhc)

Instance: TrustDemoLaoGateway
InstanceOf: Device
Title: "Lao PDR national FHIR server and info gateway"
Description: "Hosts the VHL manifests, checks passcode, expiry and consent, and records every access as an AuditEvent (J4.1)."
Usage: #example
* displayName = "Lao PDR national FHIR server and OHS FHIR Info Gateway"
* owner = Reference(TrustDemoLaoPortalOrg)

Instance: TrustDemoFamilyPhone
InstanceOf: Device
Title: "The Sengmany family's shared phone"
Description: "One phone, three profiles (Bounmy, Khamla, Somsack): the family wallet holding one VHL QR per member (J4)."
Usage: #example
* displayName = "Sengmany family phone (family wallet)"

Instance: TrustDemoClinicViewer
InstanceOf: Device
Title: "VHL viewer, Chiang Rai primary care clinic"
Description: "The point-of-care system that verifies the VHL, fetches the manifest by ITI-YY5 after the passcode is entered, and decrypts the records for viewing (J4.1): a VHL Receiver."
Usage: #example
* displayName = "Chiang Rai clinic VHL viewer"
* owner = Reference(TrustDemoChiangRaiClinic)
