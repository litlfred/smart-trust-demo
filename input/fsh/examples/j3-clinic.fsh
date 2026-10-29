// J3: the home clinic verifies both DVCs offline, imports them as
// Immunizations with provenance, evaluates the national schedule and gives
// the birth-dose OPV it finds due.

Instance: TrustDemoJ3HepBImported
InstanceOf: Immunization
Title: "J3 imported: Hep B birth dose (from a verified DVC)"
Description: "The Hep B birth dose given in Country A on 2026-10-21, imported from its DVC after the EHR verified the HCERT against XXR's DSC in the cached trust list. Not given here, so not a primary source."
Usage: #example
* status = #completed
* vaccineCode = $cvx#08 "Hep B, adolescent or pediatric"
* patient = Reference(TrustDemoChanthala)
* occurrenceDateTime = "2026-10-21"
* primarySource = false
* informationSource.concept.text = "Verified DVC (HCERT) issued by Country A (XXR)"
* location.display = "Provincial hospital, Country A (XXR)"

Instance: TrustDemoJ3BcgImported
InstanceOf: Immunization
Title: "J3 imported: BCG birth dose (from a verified DVC)"
Description: "The BCG birth dose given in Country A on 2026-10-21, imported from its DVC after the EHR verified the HCERT. Not given here, so not a primary source."
Usage: #example
* status = #completed
* vaccineCode = $cvx#19 "BCG"
* patient = Reference(TrustDemoChanthala)
* occurrenceDateTime = "2026-10-21"
* primarySource = false
* informationSource.concept.text = "Verified DVC (HCERT) issued by Country A (XXR)"
* location.display = "Provincial hospital, Country A (XXR)"

Instance: TrustDemoJ3Import
InstanceOf: Provenance
Title: "J3 provenance of the imported doses"
Description: "Records that the two imported Immunizations come from DVCs the home clinic EHR verified offline against its cached copy of the GDHCN DEV trust list."
Usage: #example
* target[+] = Reference(TrustDemoJ3HepBImported)
* target[+] = Reference(TrustDemoJ3BcgImported)
* recorded = "2026-11-04T09:30:00Z"
* activity.text = "Verified each DVC (HCERT) offline against the cached trust list, then imported it"
* agent[+].who = Reference(TrustDemoHomeClinicEhr)
* agent[+].who = Reference(TrustDemoTomasAlves)
* entity[+].role = #source
* entity[=].what.display = "DVC (HCERT, HC1 QR) for the Hep B birth dose, issued by XXR"
* entity[+].role = #source
* entity[=].what.display = "DVC (HCERT, HC1 QR) for the BCG birth dose, issued by XXR"

Instance: TrustDemoJ3Recommendation
InstanceOf: ImmunizationRecommendation
Title: "J3 schedule evaluation: birth-dose OPV due"
Description: "The national schedule run on the imported record: the Hep B and BCG birth doses count, and the birth-dose OPV is due. The schedule rules themselves are Country B's (fictional) and are not modelled here."
Usage: #example
* patient = Reference(TrustDemoChanthala)
* date = "2026-11-04T09:31:00Z"
* authority = Reference(TrustDemoHomeClinic)
* recommendation[+].vaccineCode = $cvx#182 "OPV, Unspecified formulation"
* recommendation[=].forecastStatus = http://terminology.hl7.org/CodeSystem/immunization-recommendation-status#due "Due"
* recommendation[=].doseNumber = "0"
* recommendation[=].supportingImmunization[+] = Reference(TrustDemoJ3HepBImported)
* recommendation[=].supportingImmunization[+] = Reference(TrustDemoJ3BcgImported)

Instance: TrustDemoJ3Opv0
InstanceOf: Immunization
Title: "J3 given: birth-dose OPV"
Description: "The birth-dose OPV Tomas ALVES gives at the home clinic once the schedule finds it due."
Usage: #example
* status = #completed
* vaccineCode = $cvx#182 "OPV, Unspecified formulation"
* patient = Reference(TrustDemoChanthala)
* occurrenceDateTime = "2026-11-04"
* primarySource = true
* performer.actor = Reference(TrustDemoTomasAlves)
* location.display = "District clinic, Country B (XXH)"
* basedOn = Reference(TrustDemoJ3Recommendation)
