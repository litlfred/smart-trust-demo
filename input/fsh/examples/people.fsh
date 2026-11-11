// The people, places and systems the journey examples share. The story is the
// VaxLink workshop walkthrough's (fredhersch/vaxlink): Somsak SENGMANY, an Onesan
// baby born in Taifafeki, followed over his first year. Every person here is
// fictional (AGENTS.md). Country A, the birth country, is Taifafeki, played on
// the GDHCN DEV network by test participant XXR; Country B, home, is Onesa,
// played by the test participant XXK. Neither is a real ministry's key.

Alias: $cvx = http://hl7.org/fhir/sid/cvx
Alias: $loinc = http://loinc.org
Alias: $sct = http://snomed.info/sct
Alias: $v3-RoleCode = http://terminology.hl7.org/CodeSystem/v3-RoleCode
Alias: $OnesaTmpId = http://smart.who.int/trust-demo/sid/onesa-temporary-id
Alias: $HouseholdId = http://smart.who.int/trust-demo/sid/onesa-household-id

Instance: TrustDemoSomsak
InstanceOf: TrustDemoOnesaPatient
Title: "Somsak SENGMANY (newborn)"
Description: "The subject of every journey, as the CHW registers him in Onesa (Country B) in J2: born 2025-10-28 at Kesaro Provincial Hospital, Taifafeki (Country A), with no Taifafeki identity number. Until civil registration catches up he has a temporary id. Fictional."
Usage: #example
* identifier[temporaryId].system = $OnesaTmpId
* identifier[temporaryId].value = "XXK-TMP-2025-00918"
* active = true
* name.use = #official
* name.family = "SENGMANY"
* name.given = "Somsak"
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
Description: "Somsak's mother, 26: the Holder of the two paper DVCs from J1 to J3. Fictional."
Usage: #example
* patient = Reference(TrustDemoSomsak)
* relationship = $v3-RoleCode#MTH "mother"
* name.family = "SENGMANY"
* name.given = "Khamla"
* gender = #female

Instance: TrustDemoBounmy
InstanceOf: RelatedPerson
Title: "Bounmy SENGMANY (father, head of household)"
Description: "Somsak's father, 29, head of the household: he holds the family's one shared phone and is the VHL Holder in J4. Fictional."
Usage: #example
* patient = Reference(TrustDemoSomsak)
* relationship = $v3-RoleCode#FTH "father"
* name.family = "SENGMANY"
* name.given = "Bounmy"
* gender = #male

Instance: TrustDemoKhamlaPatient
InstanceOf: Patient
Title: "Khamla SENGMANY (household member)"
Description: "Khamla as a member of the Sengmany household and a profile of her own on the family phone. In FHIR R4 a Group's members are Patients, so the household lists her as one; the RelatedPerson TrustDemoKhamla is her role as Somsak's mother. Fictional."
Usage: #example
* name.family = "SENGMANY"
* name.given = "Khamla"
* gender = #female
* link.other = Reference(TrustDemoKhamla)
* link.type = #seealso

Instance: TrustDemoBounmyPatient
InstanceOf: Patient
Title: "Bounmy SENGMANY (household member)"
Description: "Bounmy as a member of the Sengmany household and a profile of his own on the family phone. In FHIR R4 a Group's members are Patients, so the household lists him as one; the RelatedPerson TrustDemoBounmy is his role as Somsak's father. Fictional."
Usage: #example
* name.family = "SENGMANY"
* name.given = "Bounmy"
* gender = #male
* link.other = Reference(TrustDemoBounmy)
* link.type = #seealso

Instance: TrustDemoAnan
InstanceOf: Practitioner
Title: "Dr Anan (clinician, Kesaro, Taifafeki)"
Description: "Gives Somsak's birth doses and prints the DVCs (J1), and reads his record through the VHL a year later (J4.1). Fictional."
Usage: #example
* name.text = "Dr Anan"
* name.given = "Anan"
* name.prefix = "Dr"

Instance: TrustDemoVilay
InstanceOf: Practitioner
Title: "Vilay (community health worker, Village 04, Onesa)"
Description: "The CHW who finds Somsak missing from the household roster in J2. Fictional."
Usage: #example
* name.text = "Vilay"
* name.given = "Vilay"

Instance: TrustDemoChanthason
InstanceOf: Practitioner
Title: "Nurse Chanthason (Lomaru District Health Center)"
Description: "The nurse who verifies the DVCs and fits the Taifafeki doses to the Onesan schedule in J3. Fictional."
Usage: #example
* name.text = "Nurse Chanthason"
* name.given = "Chanthason"

Instance: TrustDemoKesaroHospital
InstanceOf: Organization
Title: "Kesaro Provincial Hospital, Taifafeki (Country A)"
Description: "The birth hospital of J1. Its DVCs are signed with the DSC of GDHCN DEV test participant XXR, which plays Taifafeki in the demonstrator."
Usage: #example
* name = "Kesaro Provincial Hospital (demonstrator)"
* contact.address.country = "XXR"

Instance: TrustDemoLomaruDhc
InstanceOf: Organization
Title: "Lomaru District Health Center, Onesa (Country B)"
Description: "The district health center of J3 and of Somsak's later Onesan doses."
Usage: #example
* name = "Lomaru District Health Center (demonstrator)"
* contact.address.country = "XXK"

Instance: TrustDemoOnesaPortalOrg
InstanceOf: Organization
Title: "Onesa national health portal (Country B, XXK)"
Description: "The national service that hosts the family's records, issues their VHLs (J4.0) and logs every access (J4.1). On the GDHCN DEV network it is the test participant XXK."
Usage: #example
* name = "Onesa national health portal (demonstrator, GDHCN DEV participant XXK)"
* contact.address.country = "XXK"

Instance: TrustDemoKesaroClinic
InstanceOf: Organization
Title: "Kesaro primary care clinic, Taifafeki (J4.1)"
Description: "Where Dr Anan sees Somsak a year after his birth, back in Country A."
Usage: #example
* name = "Kesaro primary care clinic (demonstrator)"
* contact.address.country = "XXR"

Instance: TrustDemoChwApp
InstanceOf: Device
Title: "CHW app (OHS, community configuration), Onesa"
Description: "The offline app on Vilay's phone (J2): household registration, triage read of foreign DVCs (STT-VER-011), referral."
Usage: #example
* deviceName[+].name = "CHW app, Village 04 (offline)"
* deviceName[=].type = #user-friendly-name

Instance: TrustDemoDhcEhr
InstanceOf: Device
Title: "District health center EHR (OHS, facility configuration), Onesa"
Description: "The clinic tablet's record system that verifies the DVCs offline against its cached GDHCN trust list, imports them and evaluates the schedule (J3)."
Usage: #example
* deviceName[+].name = "Lomaru District Health Center EHR"
* deviceName[=].type = #user-friendly-name
* owner = Reference(TrustDemoLomaruDhc)

Instance: TrustDemoOnesaGateway
InstanceOf: Device
Title: "Onesa national FHIR server and info gateway"
Description: "Hosts the VHL manifests, checks passcode, expiry and consent, and records every access as an AuditEvent (J4.1)."
Usage: #example
* deviceName[+].name = "Onesa national FHIR server and OHS FHIR Info Gateway"
* deviceName[=].type = #user-friendly-name
* owner = Reference(TrustDemoOnesaPortalOrg)

Instance: TrustDemoFamilyPhone
InstanceOf: Device
Title: "The Sengmany family's shared phone"
Description: "One phone, three profiles (Bounmy, Khamla, Somsak): the family wallet holding one VHL QR per member (J4)."
Usage: #example
* deviceName[+].name = "Sengmany family phone (family wallet)"
* deviceName[=].type = #user-friendly-name

Instance: TrustDemoClinicViewer
InstanceOf: Device
Title: "VHL viewer, Kesaro primary care clinic"
Description: "The point-of-care system that verifies the VHL, fetches the manifest by ITI-YY5 after the passcode is entered, and decrypts the records for viewing (J4.1): a VHL Receiver."
Usage: #example
* deviceName[+].name = "Kesaro clinic VHL viewer"
* deviceName[=].type = #user-friendly-name
* owner = Reference(TrustDemoKesaroClinic)
