// J2a and J2b, Village 04, Lao PDR, 2025-11-18 (T0 + 3 weeks). Vilay adds
// Somsack to the Sengmany household offline, scans the two paper DVCs without
// verifying them, saves the doses as reported by the family, and refers him
// to the district health center. Everything is queued on her phone and syncs
// when it next has a signal.

Instance: TrustDemoHousehold
InstanceOf: TrustDemoLaoHousehold
Title: "J2a the Sengmany household (HH-LAO-204)"
Description: "The household roster Vilay updates on her offline phone: Somsack is added beside his mother and father."
Usage: #example
* identifier[household].system = $HouseholdId
* identifier[household].value = "HH-LAO-204"
* type = #person
* membership = #enumerated
* code = $v3-RoleCode#FAMMEMB "family member"
* code.text = "Household"
* name = "Sengmany household"
* quantity = 3
* managingEntity = Reference(TrustDemoBounmy)
* member[+].entity = Reference(TrustDemoBounmy)
* member[+].entity = Reference(TrustDemoKhamla)
* member[+].entity = Reference(TrustDemoSomsack)
* member[=].period.start = "2025-11-18"

Instance: TrustDemoHouseholdRegistration
InstanceOf: Questionnaire
Title: "J2a newborn registration form (structured data capture)"
Description: "The form the CHW app renders offline (OHS Structured Data Capture) to add a newborn to a household and note any foreign vaccination cards."
Usage: #definition
* url = "http://smart.who.int/trust-demo/Questionnaire/TrustDemoHouseholdRegistration"
* name = "TrustDemoHouseholdRegistration"
* title = "Add a newborn to the household"
* status = #draft
* experimental = true
* subjectType = #Patient
* item[+].linkId = "household"
* item[=].text = "Household id"
* item[=].type = #string
* item[=].required = true
* item[+].linkId = "given"
* item[=].text = "Child's given name"
* item[=].type = #string
* item[=].required = true
* item[+].linkId = "family"
* item[=].text = "Child's family name"
* item[=].type = #string
* item[=].required = true
* item[+].linkId = "birthDate"
* item[=].text = "Date of birth"
* item[=].type = #date
* item[=].required = true
* item[+].linkId = "birthCountry"
* item[=].text = "Country of birth"
* item[=].type = #string
* item[+].linkId = "foreignCards"
* item[=].text = "Does the family hold vaccination cards from abroad?"
* item[=].type = #boolean

Instance: TrustDemoJ2Registration
InstanceOf: TrustDemoLaoRegistration
Title: "J2a Somsack's registration, as captured offline"
Description: "Vilay's answers on the newborn registration form, saved on the phone with no signal and synced later."
Usage: #example
* questionnaire = Canonical(TrustDemoHouseholdRegistration)
* status = #completed
* subject = Reference(TrustDemoSomsack)
* authored = "2025-11-18T10:05:00+07:00"
* author = Reference(TrustDemoVilay)
* source = Reference(TrustDemoBounmy)
* item[+].linkId = "household"
* item[=].answer.valueString = "HH-LAO-204"
* item[+].linkId = "given"
* item[=].answer.valueString = "Somsack"
* item[+].linkId = "family"
* item[=].answer.valueString = "SENGMANY"
* item[+].linkId = "birthDate"
* item[=].answer.valueDate = "2025-10-28"
* item[+].linkId = "birthCountry"
* item[=].answer.valueString = "Thailand"
* item[+].linkId = "foreignCards"
* item[=].answer.valueBoolean = true

Instance: TrustDemoJ2HepBReported
InstanceOf: TrustDemoLaoReportedImmunization
Title: "J2b reported: Hep B birth dose (DVC read, not verified)"
Description: "The Hep B birth dose as the CHW app saves it after reading the paper DVC offline without verifying it (STT-VER-011): reported by the family, primarySource false, only the issuer's product coding."
Usage: #example
* status = #completed
* vaccineCode = TrustDemoVaccineProduct#vp-hepb-peds-monovalent "Hepatitis B vaccine, paediatric, monovalent"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-10-28"
* primarySource = false
* informationSource.reference = Reference(TrustDemoKhamla)
* lotNumber = "TH-4821"
* location.display = "Chiang Rai Provincial Hospital, Thailand"
* note.text = "Read from a paper DVC without verifying its signature (triage read): reported, not verified."

Instance: TrustDemoJ2BcgReported
InstanceOf: TrustDemoLaoReportedImmunization
Title: "J2b reported: BCG birth dose (DVC read, not verified)"
Description: "The BCG birth dose as the CHW app saves it after the unverified read: reported by the family, primarySource false."
Usage: #example
* status = #completed
* vaccineCode = TrustDemoVaccineProduct#vp-bcg-freeze-dried "BCG vaccine, freeze-dried"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-10-28"
* primarySource = false
* informationSource.reference = Reference(TrustDemoKhamla)
* lotNumber = "TH-9012"
* location.display = "Chiang Rai Provincial Hospital, Thailand"
* note.text = "Read from a paper DVC without verifying its signature (triage read): reported, not verified."

Instance: TrustDemoJ2Referral
InstanceOf: TrustDemoLaoReferral
Title: "J2b referral to the district health center"
Description: "Vilay's referral of Somsack to Vientiane District Health Center: verify the two foreign DVCs and fit the doses to the national schedule."
Usage: #example
* status = #active
* intent = #order
* priority = #routine
* code.concept = $sct#3457005 "Patient referral"
* code.concept.text = "Verify foreign paper DVCs and map the birth doses to the national schedule"
* subject = Reference(TrustDemoSomsack)
* authoredOn = "2025-11-18T10:20:00+07:00"
* requester = Reference(TrustDemoVilay)
* performer = Reference(TrustDemoVientianeDhc)
* reason[+].concept.text = "Unverified foreign vaccination cards presented on a home visit (primarySource false)"
* supportingInfo[+].reference = Reference(TrustDemoJ2HepBReported)
* supportingInfo[+].reference = Reference(TrustDemoJ2BcgReported)
