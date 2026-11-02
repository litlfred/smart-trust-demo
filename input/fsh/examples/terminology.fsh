// The vaccine codings of the journeys. Both code systems are illustrative
// stand-ins, as in the VaxLink walkthrough: TrustDemoVaccineProduct stands in
// for WHO PreQual product ids (the issuer's coding, as signed in a DVC) and
// TrustDemoLaoEpiSchedule for a national schedule's antigen-and-dose codes.
// Neither is an official code system; real deployments use the WHO PreQual
// ids and the country's own schedule codes.

CodeSystem: TrustDemoVaccineProduct
Id: TrustDemoVaccineProduct
Title: "Vaccine products (illustrative PreQual-style codes)"
Description: "Illustrative product codes in the style of WHO PreQual product ids, as the VaxLink walkthrough uses them: the issuer's coding of each dose. Not WHO PreQual ids."
* ^experimental = true
* ^caseSensitive = true
* #vp-hepb-peds-monovalent "Hepatitis B vaccine, paediatric, monovalent"
* #vp-bcg-freeze-dried "BCG vaccine, freeze-dried"
* #vp-pentavalent-liquid "DTP-HepB-Hib (pentavalent), liquid"
* #vp-bopv-drops "Bivalent oral polio vaccine (bOPV), drops"
* #vp-pcv-13-dose "Pneumococcal conjugate vaccine (PCV)"
* #vp-mr-freeze-dried "Measles-rubella vaccine, freeze-dried"

CodeSystem: TrustDemoLaoEpiSchedule
Id: TrustDemoLaoEpiSchedule
Title: "National schedule antigen-dose codes (illustrative, Lao PDR)"
Description: "Illustrative antigen-and-dose codes of a national immunization schedule, as the VaxLink walkthrough names them for Lao PDR. Not the official Lao EPI coding."
* ^experimental = true
* ^caseSensitive = true
* #LAO-EPI-HEPB-BD "Hepatitis B birth dose"
* #LAO-EPI-BCG "BCG"
* #LAO-EPI-PENTA-1 "Pentavalent (DTP-HepB-Hib), dose 1"
* #LAO-EPI-OPV-1 "bOPV, dose 1"
* #LAO-EPI-PCV-1 "PCV, dose 1"
* #LAO-EPI-MR-1 "Measles-rubella, dose 1"

ValueSet: TrustDemoVaccineProducts
Id: TrustDemoVaccineProducts
Title: "Vaccine products of the journeys"
Description: "Every product code of TrustDemoVaccineProduct: the source of the national ConceptMap."
* ^experimental = true
* include codes from system TrustDemoVaccineProduct

ValueSet: TrustDemoLaoEpiScheduleCodes
Id: TrustDemoLaoEpiScheduleCodes
Title: "National schedule codes of the journeys"
Description: "Every code of TrustDemoLaoEpiSchedule: the target of the national ConceptMap."
* ^experimental = true
* include codes from system TrustDemoLaoEpiSchedule

Instance: TrustDemoProductToLaoEpi
InstanceOf: ConceptMap
Title: "J3 map: vaccine product to national schedule dose"
Description: "The national map the clinic EHR uses in J3 to add the schedule code beside the issuer's product code, which it never replaces. The Hep B product had no entry until Nurse Chanthasone confirmed its equivalence on 2025-11-25 (see TrustDemoJ3Adjudication); her decision is recorded here so the next clinic need not make it again."
Usage: #definition
* url = "http://smart.who.int/trust-demo/ConceptMap/TrustDemoProductToLaoEpi"
* name = "TrustDemoProductToLaoEpi"
* status = #draft
* experimental = true
* sourceScopeCanonical = Canonical(TrustDemoVaccineProducts)
* targetScopeCanonical = Canonical(TrustDemoLaoEpiScheduleCodes)
* group[+].source = Canonical(TrustDemoVaccineProduct)
* group[=].target = Canonical(TrustDemoLaoEpiSchedule)
* group[=].element[+].code = #vp-hepb-peds-monovalent
* group[=].element[=].target[+].code = #LAO-EPI-HEPB-BD
* group[=].element[=].target[=].relationship = #equivalent
* group[=].element[=].target[=].comment = "Added from the nurse's adjudication at Vientiane District Health Center, 2025-11-25: a monovalent paediatric Hep B dose given within 24 hours of birth counts as the schedule's birth dose."
* group[=].element[+].code = #vp-bcg-freeze-dried
* group[=].element[=].target[+].code = #LAO-EPI-BCG
* group[=].element[=].target[=].relationship = #equivalent
* group[=].element[+].code = #vp-pentavalent-liquid
* group[=].element[=].target[+].code = #LAO-EPI-PENTA-1
* group[=].element[=].target[=].relationship = #equivalent
* group[=].element[+].code = #vp-bopv-drops
* group[=].element[=].target[+].code = #LAO-EPI-OPV-1
* group[=].element[=].target[=].relationship = #equivalent
* group[=].element[+].code = #vp-pcv-13-dose
* group[=].element[=].target[+].code = #LAO-EPI-PCV-1
* group[=].element[=].target[=].relationship = #equivalent
* group[=].element[+].code = #vp-mr-freeze-dried
* group[=].element[=].target[+].code = #LAO-EPI-MR-1
* group[=].element[=].target[=].relationship = #equivalent

Instance: TrustDemoLaoInfantSchedule
InstanceOf: PlanDefinition
Title: "J3 national infant schedule (illustrative excerpt)"
Description: "The part of the national schedule the J3 evaluation needs: birth doses, the 6-week doses and measles-rubella at 9 months. Illustrative; the schedule rules are not executable here."
Usage: #definition
* url = "http://smart.who.int/trust-demo/PlanDefinition/TrustDemoLaoInfantSchedule"
* name = "TrustDemoLaoInfantSchedule"
* title = "National infant immunization schedule (illustrative excerpt)"
* status = #draft
* experimental = true
* type = http://terminology.hl7.org/CodeSystem/plan-definition-type#clinical-protocol
* action[+].title = "Birth doses"
* action[=].code = TrustDemoLaoEpiSchedule#LAO-EPI-HEPB-BD "Hepatitis B birth dose"
* action[=].timingAge = 0 'd' "days"
* action[+].title = "BCG"
* action[=].code = TrustDemoLaoEpiSchedule#LAO-EPI-BCG "BCG"
* action[=].timingAge = 0 'd' "days"
* action[+].title = "6 weeks: pentavalent 1"
* action[=].code = TrustDemoLaoEpiSchedule#LAO-EPI-PENTA-1 "Pentavalent (DTP-HepB-Hib), dose 1"
* action[=].timingAge = 6 'wk' "weeks"
* action[+].title = "6 weeks: bOPV 1"
* action[=].code = TrustDemoLaoEpiSchedule#LAO-EPI-OPV-1 "bOPV, dose 1"
* action[=].timingAge = 6 'wk' "weeks"
* action[+].title = "6 weeks: PCV 1"
* action[=].code = TrustDemoLaoEpiSchedule#LAO-EPI-PCV-1 "PCV, dose 1"
* action[=].timingAge = 6 'wk' "weeks"
* action[+].title = "9 months: measles-rubella 1"
* action[=].code = TrustDemoLaoEpiSchedule#LAO-EPI-MR-1 "Measles-rubella, dose 1"
* action[=].timingAge = 9 'mo' "months"
