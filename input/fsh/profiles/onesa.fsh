// Country B, Onesa, home: the CHW visit (J2), the district clinic (J3) and
// the national portal that issues the family's VHLs and logs every access
// (J4). Onesa is played on the GDHCN DEV network by the fictional
// participant XXK. Demonstrator profiles: they show which elements each step
// relies on, not any real Onesan national specification.

Alias: $OnesaTmpId = http://smart.who.int/trust-demo/sid/onesa-temporary-id
Alias: $HouseholdId = http://smart.who.int/trust-demo/sid/onesa-household-id

Profile: TrustDemoOnesaPatient
Parent: Patient
Id: TrustDemoOnesaPatient
Title: "Onesa: child registered by the community health worker"
Description: """
How it is used: J2 onwards. Vilay registers Somsak on a home visit, and the same patient carries every Onesan record that follows: the verified Taifafeki doses, the Onesan doses and the summary shared in J4.

Why: a child born abroad is not in the Onesan civil registry yet. A temporary id lets the CHW, the district clinic and the national portal all refer to the same child until civil registration catches up. The parents are recorded as contacts, because they hold the paper cards and later the family's VHLs.
"""
* identifier 1..* MS
* identifier ^slicing.discriminator.type = #value
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
* identifier contains temporaryId 0..1 MS
* identifier[temporaryId].system = $OnesaTmpId
* identifier[temporaryId].value 1..1
* name 1..* MS
* birthDate 1..1 MS
* contact MS

Profile: TrustDemoOnesaHousehold
Parent: Group
Id: TrustDemoOnesaHousehold
Title: "Onesa: household on the CHW's roster"
Description: """
How it is used: J2a. The CHW finds that a newborn is missing from the household roster and adds Somsak as a member.

Why: Onesan community health work is organized by household. The roster is how a CHW notices that a child is missing, and it is the unit the family phone shares under in J4 (one phone, three profiles).
"""
* identifier 1..* MS
* identifier ^slicing.discriminator.type = #value
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
* identifier contains household 1..1 MS
* identifier[household].system = $HouseholdId
* type = #person
* actual = true
* member 1..* MS
* member.entity only Reference(Patient)

Profile: TrustDemoOnesaRegistration
Parent: QuestionnaireResponse
Id: TrustDemoOnesaRegistration
Title: "Onesa: newborn registration captured offline"
Description: """
How it is used: J2a. These are the CHW's answers on the newborn registration form, which the app renders with Structured Data Capture and saves with no signal.

Why: in Onesa the form is the configuration, not code. A ministry can change the questions without shipping a new app. The answers are kept so that the Patient and Group extracted from them can always be traced back to what was asked and who answered.
"""
* questionnaire = "http://smart.who.int/trust-demo/Questionnaire/TrustDemoHouseholdRegistration"
* subject 1..1 MS
* subject only Reference(TrustDemoOnesaPatient)
* authored 1..1 MS
* author 1..1 MS
* source MS

Profile: TrustDemoOnesaReportedImmunization
Parent: Immunization
Id: TrustDemoOnesaReportedImmunization
Title: "Onesa: foreign dose as reported (not yet verified)"
Description: """
How it is used: J2b. The CHW app reads each Taifafeki paper DVC offline without checking its signature, and saves the dose like this.

Why: a CHW phone may have no trust list and no signal, but the doses should not be lost. Recording them with primarySource false, the paper card as the report origin and the family named in the note keeps them visibly "reported, not verified". The schedule will not count them until a clinic verifies them (J3). Only the issuer's product code is present, because mapping to the Onesan schedule is a clinical step for later.
"""
* status = #completed
* patient only Reference(TrustDemoOnesaPatient)
* primarySource = false
* reportOrigin 1..1 MS
* note 1..* MS
* lotNumber MS

Profile: TrustDemoOnesaImmunization
Parent: Immunization
Id: TrustDemoOnesaImmunization
Title: "Onesa: dose on the national schedule"
Description: """
How it is used: J3 and after. These are the Taifafeki birth doses once the district clinic has verified them, and every dose given in Onesa.

Why: the Onesan schedule engine works on Onesan EPI codes, so each dose must carry one. A dose that came from abroad keeps the issuer's product code beside the Onesan one, added through the ConceptMap and confirmed by the nurse. Nothing the other country said is overwritten. A verified foreign dose is recorded from its primary source, the signing hospital, and its Provenance says how it was verified.
"""
* status = #completed
* vaccineCode.coding ^slicing.discriminator.type = #value
* vaccineCode.coding ^slicing.discriminator.path = "system"
* vaccineCode.coding ^slicing.rules = #open
* vaccineCode.coding contains onesaEpi 1..1 MS and product 0..1 MS and cvx 0..1
* vaccineCode.coding[cvx].system = "http://hl7.org/fhir/sid/cvx"
* vaccineCode.coding[onesaEpi] from TrustDemoOnesaEpiScheduleCodes (required)
* vaccineCode.coding[onesaEpi].system = Canonical(TrustDemoOnesaEpiSchedule)
* vaccineCode.coding[product] from TrustDemoVaccineProducts (required)
* vaccineCode.coding[product].system = Canonical(TrustDemoVaccineProduct)
* patient only Reference(TrustDemoOnesaPatient)
* primarySource = true
* lotNumber MS
* protocolApplied MS

Profile: TrustDemoOnesaReferral
Parent: ServiceRequest
Id: TrustDemoOnesaReferral
Title: "Onesa: CHW referral to verify foreign cards"
Description: """
How it is used: J2b. The CHW refers Somsak to the district health center to have his foreign cards verified and his doses fitted to the Onesan schedule.

Why: the CHW cannot verify a DVC on the phone, but the clinic can. The referral points at the reported doses it is about, so the clinic knows exactly what to check, and the CHW can see when it is done.
"""
* subject only Reference(TrustDemoOnesaPatient)
* requester 1..1 MS
* performer 1..* MS
* supportingInfo 1..* MS

Profile: TrustDemoOnesaDvcVerification
Parent: Provenance
Id: TrustDemoOnesaDvcVerification
Title: "Onesa: foreign DVC verified against the GDHCN trust list"
Description: """
How it is used: J3a. The district EHR verifies each Taifafeki DVC offline against its cached copy of the GDHCN trust list, then imports the dose. This record says so.

Why: a verified dose replaces a reported one, so the record must show who verified what, against which policy, and which reported doses it removes. Anyone who later doubts a dose can follow this record back to the signed certificate and the issuing country's key.
"""
* target 1..* MS
* target only Reference(TrustDemoOnesaImmunization)
* policy 1..* MS
* activity 1..1 MS
* agent 2..* MS
* entity 1..* MS

Profile: TrustDemoOnesaVhlAccess
Parent: AuditEvent
Id: TrustDemoOnesaVhlAccess
Title: "Onesa: every VHL access logged at home"
Description: """
How it is used: J4.1. The Onesan national gateway records each attempt by a clinic abroad to fetch a family member's VHL manifest, the refused ones included.

Why: the family shares a link, not a copy, and the data stays in Onesa. Logging every access at home, following IHE Basic Audit Log Patterns, is what lets the family and the ministry see who looked, from where and when. A wrong passcode is logged too.
"""
* recorded MS
* outcome 1..1 MS
* agent 2..* MS
* source.observer MS
* entity 1..* MS
