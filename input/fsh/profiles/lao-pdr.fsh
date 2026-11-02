// Country B, Lao PDR, home: the CHW visit (J2), the district clinic (J3) and
// the national portal that issues the family's VHLs and logs every access
// (J4). Lao PDR is played on the GDHCN DEV network by the fictional
// participant XXH. Demonstrator profiles: they show which elements each step
// relies on, not any real Lao national specification.

Alias: $LaoTmpId = http://smart.who.int/trust-demo/sid/lao-temporary-id
Alias: $HouseholdId = http://smart.who.int/trust-demo/sid/lao-household-id

Profile: TrustDemoLaoPatient
Parent: Patient
Id: TrustDemoLaoPatient
Title: "Lao PDR: child registered by the community health worker"
Description: """
How it is used: J2 onwards. Vilay registers Somsack on a home visit, and the same patient carries every Lao record that follows: the verified Thai doses, the Lao doses and the summary shared in J4.

Why: a child born abroad is not in the Lao civil registry yet. A temporary id lets the CHW, the district clinic and the national portal all refer to the same child until civil registration catches up. The parents are recorded as contacts, because they hold the paper cards and later the family's VHLs.
"""
* identifier 1..* MS
* identifier ^slicing.discriminator.type = #value
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
* identifier contains temporaryId 0..1 MS
* identifier[temporaryId].system = $LaoTmpId
* identifier[temporaryId].value 1..1
* name 1..* MS
* birthDate 1..1 MS
* contact MS

Profile: TrustDemoLaoHousehold
Parent: Group
Id: TrustDemoLaoHousehold
Title: "Lao PDR: household on the CHW's roster"
Description: """
How it is used: J2a. The CHW finds that a newborn is missing from the household roster and adds Somsack as a member.

Why: Lao community health work is organized by household. The roster is how a CHW notices that a child is missing, and it is the unit the family phone shares under in J4 (one phone, three profiles).
"""
* identifier 1..* MS
* identifier ^slicing.discriminator.type = #value
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
* identifier contains household 1..1 MS
* identifier[household].system = $HouseholdId
* type = #person
* membership = #enumerated
* member 1..* MS
* member.entity only Reference(TrustDemoLaoPatient or RelatedPerson)

Profile: TrustDemoLaoRegistration
Parent: QuestionnaireResponse
Id: TrustDemoLaoRegistration
Title: "Lao PDR: newborn registration captured offline"
Description: """
How it is used: J2a. These are the CHW's answers on the newborn registration form, which the app renders with Structured Data Capture and saves with no signal.

Why: in Lao PDR the form is the configuration, not code. A ministry can change the questions without shipping a new app. The answers are kept so that the Patient and Group extracted from them can always be traced back to what was asked and who answered.
"""
* questionnaire = "http://smart.who.int/trust-demo/Questionnaire/TrustDemoHouseholdRegistration"
* subject 1..1 MS
* subject only Reference(TrustDemoLaoPatient)
* authored 1..1 MS
* author 1..1 MS
* source MS

Profile: TrustDemoLaoReportedImmunization
Parent: Immunization
Id: TrustDemoLaoReportedImmunization
Title: "Lao PDR: foreign dose as reported (not yet verified)"
Description: """
How it is used: J2b. The CHW app reads each Thai paper DVC offline without checking its signature, and saves the dose like this.

Why: a CHW phone may have no trust list and no signal, but the doses should not be lost. Recording them with primarySource false and the family as the information source keeps them visibly "reported, not verified". The schedule will not count them until a clinic verifies them (J3). Only the issuer's product code is present, because mapping to the Lao schedule is a clinical step for later.
"""
* status = #completed
* patient only Reference(TrustDemoLaoPatient)
* primarySource = false
* informationSource 1..1 MS
* note 1..* MS
* lotNumber MS

Profile: TrustDemoLaoImmunization
Parent: Immunization
Id: TrustDemoLaoImmunization
Title: "Lao PDR: dose on the national schedule"
Description: """
How it is used: J3 and after. These are the Thai birth doses once the district clinic has verified them, and every dose given in Lao PDR.

Why: the Lao schedule engine works on Lao EPI codes, so each dose must carry one. A dose that came from abroad keeps the issuer's product code beside the Lao one, added through the ConceptMap and confirmed by the nurse. Nothing the other country said is overwritten. A verified foreign dose is recorded from its primary source, the signing hospital, and its Provenance says how it was verified.
"""
* status = #completed
* vaccineCode.coding ^slicing.discriminator.type = #value
* vaccineCode.coding ^slicing.discriminator.path = "system"
* vaccineCode.coding ^slicing.rules = #open
* vaccineCode.coding contains laoEpi 1..1 MS and product 0..1 MS and cvx 0..1
* vaccineCode.coding[cvx].system = "http://hl7.org/fhir/sid/cvx"
* vaccineCode.coding[laoEpi] from TrustDemoLaoEpiScheduleCodes (required)
* vaccineCode.coding[laoEpi].system = Canonical(TrustDemoLaoEpiSchedule)
* vaccineCode.coding[product] from TrustDemoVaccineProducts (required)
* vaccineCode.coding[product].system = Canonical(TrustDemoVaccineProduct)
* patient only Reference(TrustDemoLaoPatient)
* primarySource = true
* lotNumber MS
* protocolApplied MS

Profile: TrustDemoLaoReferral
Parent: ServiceRequest
Id: TrustDemoLaoReferral
Title: "Lao PDR: CHW referral to verify foreign cards"
Description: """
How it is used: J2b. The CHW refers Somsack to the district health center to have his foreign cards verified and his doses fitted to the Lao schedule.

Why: the CHW cannot verify a DVC on the phone, but the clinic can. The referral points at the reported doses it is about, so the clinic knows exactly what to check, and the CHW can see when it is done.
"""
* subject only Reference(TrustDemoLaoPatient)
* requester 1..1 MS
* performer 1..* MS
* supportingInfo 1..* MS

Profile: TrustDemoLaoDvcVerification
Parent: Provenance
Id: TrustDemoLaoDvcVerification
Title: "Lao PDR: foreign DVC verified against the GDHCN trust list"
Description: """
How it is used: J3a. The district EHR verifies each Thai DVC offline against its cached copy of the GDHCN trust list, then imports the dose. This record says so.

Why: a verified dose replaces a reported one, so the record must show who verified what, against which policy, and which reported doses it removes. Anyone who later doubts a dose can follow this record back to the signed certificate and the issuing country's key.
"""
* target 1..* MS
* target only Reference(TrustDemoLaoImmunization)
* policy 1..* MS
* activity 1..1 MS
* agent 2..* MS
* entity 1..* MS

Profile: TrustDemoLaoVhlAccess
Parent: AuditEvent
Id: TrustDemoLaoVhlAccess
Title: "Lao PDR: every VHL access logged at home"
Description: """
How it is used: J4.1. The Lao national gateway records each attempt by a clinic abroad to fetch a family member's VHL manifest, the refused ones included.

Why: the family shares a link, not a copy, and the data stays in Lao PDR. Logging every access at home, following IHE Basic Audit Log Patterns, is what lets the family and the ministry see who looked, from where and when. A wrong passcode is logged too.
"""
* recorded MS
* outcome 1..1 MS
* agent 2..* MS
* source.observer MS
* entity 1..* MS
