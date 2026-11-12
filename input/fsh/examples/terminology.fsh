// The vaccine codings of the journeys. Both code systems are illustrative
// stand-ins, as in the VaxLink walkthrough: TrustDemoVaccineProduct stands in
// for WHO PreQual product ids (the issuer's coding, as signed in a DVC) and
// TrustDemoOnesaEpiSchedule for a national schedule's antigen-and-dose codes.
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

CodeSystem: TrustDemoOnesaEpiSchedule
Id: TrustDemoOnesaEpiSchedule
Title: "National schedule antigen-dose codes (illustrative, Onesa)"
Description: "Illustrative antigen-and-dose codes of a national immunization schedule, as the VaxLink walkthrough names them for Onesa. Not the official Onesan EPI coding."
* ^experimental = true
* ^caseSensitive = true
* #XXK-EPI-HEPB-BD "Hepatitis B birth dose"
* #XXK-EPI-BCG "BCG"
* #XXK-EPI-PENTA-1 "Pentavalent (DTP-HepB-Hib), dose 1"
* #XXK-EPI-OPV-1 "bOPV, dose 1"
* #XXK-EPI-PCV-1 "PCV, dose 1"
* #XXK-EPI-MR-1 "Measles-rubella, dose 1"

ValueSet: TrustDemoVaccineProducts
Id: TrustDemoVaccineProducts
Title: "Vaccine products of the journeys"
Description: "Every product code of TrustDemoVaccineProduct: the source of the national ConceptMap."
* ^experimental = true
* include codes from system TrustDemoVaccineProduct

ValueSet: TrustDemoOnesaEpiScheduleCodes
Id: TrustDemoOnesaEpiScheduleCodes
Title: "National schedule codes of the journeys"
Description: "Every code of TrustDemoOnesaEpiSchedule: the target of the national ConceptMap."
* ^experimental = true
* include codes from system TrustDemoOnesaEpiSchedule

Instance: TrustDemoProductToOnesaEpi
InstanceOf: ConceptMap
Title: "J3 map: vaccine product to national schedule dose"
Description: "The national map the clinic EHR uses in J3 to add the schedule code beside the issuer's product code, which it never replaces. The Hep B product had no entry until Nurse Chanthason confirmed its equivalence on 2025-11-25 (see TrustDemoJ3Adjudication); her decision is recorded here so the next clinic need not make it again."
Usage: #definition
* url = "http://smart.who.int/trust-demo/ConceptMap/TrustDemoProductToOnesaEpi"
* name = "TrustDemoProductToOnesaEpi"
* status = #draft
* experimental = true
* sourceCanonical = Canonical(TrustDemoVaccineProducts)
* targetCanonical = Canonical(TrustDemoOnesaEpiScheduleCodes)
* group[+].source = Canonical(TrustDemoVaccineProduct)
* group[=].target = Canonical(TrustDemoOnesaEpiSchedule)
* group[=].element[+].code = #vp-hepb-peds-monovalent
* group[=].element[=].target[+].code = #XXK-EPI-HEPB-BD
* group[=].element[=].target[=].equivalence = #equivalent
* group[=].element[=].target[=].comment = "Added from the nurse's adjudication at Lomaru District Health Center, 2025-11-25: a monovalent paediatric Hep B dose given within 24 hours of birth counts as the schedule's birth dose."
* group[=].element[+].code = #vp-bcg-freeze-dried
* group[=].element[=].target[+].code = #XXK-EPI-BCG
* group[=].element[=].target[=].equivalence = #equivalent
* group[=].element[+].code = #vp-pentavalent-liquid
* group[=].element[=].target[+].code = #XXK-EPI-PENTA-1
* group[=].element[=].target[=].equivalence = #equivalent
* group[=].element[+].code = #vp-bopv-drops
* group[=].element[=].target[+].code = #XXK-EPI-OPV-1
* group[=].element[=].target[=].equivalence = #equivalent
* group[=].element[+].code = #vp-pcv-13-dose
* group[=].element[=].target[+].code = #XXK-EPI-PCV-1
* group[=].element[=].target[=].equivalence = #equivalent
* group[=].element[+].code = #vp-mr-freeze-dried
* group[=].element[=].target[+].code = #XXK-EPI-MR-1
* group[=].element[=].target[=].equivalence = #equivalent

Instance: TrustDemoOnesaInfantSchedule
InstanceOf: PlanDefinition
Title: "J3 national infant schedule (illustrative excerpt)"
Description: "The part of the national schedule the J3 evaluation needs: birth doses, the 6-week doses and measles-rubella at 9 months. Illustrative; the schedule rules are not executable here."
Usage: #definition
* url = "http://smart.who.int/trust-demo/PlanDefinition/TrustDemoOnesaInfantSchedule"
* name = "TrustDemoOnesaInfantSchedule"
* title = "National infant immunization schedule (illustrative excerpt)"
* status = #draft
* experimental = true
* type = http://terminology.hl7.org/CodeSystem/plan-definition-type#clinical-protocol
* action[+].title = "Birth doses"
* action[=].code = TrustDemoOnesaEpiSchedule#XXK-EPI-HEPB-BD "Hepatitis B birth dose"
* action[=].timingAge = 0 'd' "days"
* action[+].title = "BCG"
* action[=].code = TrustDemoOnesaEpiSchedule#XXK-EPI-BCG "BCG"
* action[=].timingAge = 0 'd' "days"
* action[+].title = "6 weeks: pentavalent 1"
* action[=].code = TrustDemoOnesaEpiSchedule#XXK-EPI-PENTA-1 "Pentavalent (DTP-HepB-Hib), dose 1"
* action[=].timingAge = 6 'wk' "weeks"
* action[+].title = "6 weeks: bOPV 1"
* action[=].code = TrustDemoOnesaEpiSchedule#XXK-EPI-OPV-1 "bOPV, dose 1"
* action[=].timingAge = 6 'wk' "weeks"
* action[+].title = "6 weeks: PCV 1"
* action[=].code = TrustDemoOnesaEpiSchedule#XXK-EPI-PCV-1 "PCV, dose 1"
* action[=].timingAge = 6 'wk' "weeks"
* action[+].title = "9 months: measles-rubella 1"
* action[=].code = TrustDemoOnesaEpiSchedule#XXK-EPI-MR-1 "Measles-rubella, dose 1"
* action[=].timingAge = 9 'mo' "months"

// The trust domains of the journeys. A GDHCN trust domain scopes what a
// participant's keys may sign; the DID trust list names it for each key, and a
// verifier accepts a certificate only under a domain it knows. These codes are
// the demo's own, invented for the Onesa and Taifafeki journeys, in the style
// of the GDHCN Trust Domains CodeSystem of smart-trust
// (http://smart.who.int/trust/CodeSystem/Domains-DEV). They are not GDHCN
// trust domains.

CodeSystem: TrustDemoTrustDomain
Id: TrustDemoTrustDomain
Title: "Trust domains of the journeys (illustrative)"
Description: "Illustrative GDHCN-style trust domains for the demo's journeys: the scope under which each certificate in J1 to J4.1 is signed and verified. Invented for the demo, modelled on the GDHCN Trust Domains of SMART Trust; not GDHCN trust domains."
* ^experimental = true
* ^caseSensitive = true
* #DEMO-DVC "Demo: Digital Vaccination Certificate" "Routine-immunization DVCs (HCERT) signed per dose by a birth clinic system and verified by a home clinic EHR (J1, J3)."
* #DEMO-VHL "Demo: Verifiable Health Link" "Verifiable Health Links (HCERT) to a patient summary, created on the national portal and resolved at a point of care abroad (J4.0, J4.1)."

ValueSet: TrustDemoTrustDomains
Id: TrustDemoTrustDomains
Title: "Trust domains of the journeys"
Description: "Every code of TrustDemoTrustDomain: the trust domains a verifier in the journeys accepts."
* ^experimental = true
* include codes from system TrustDemoTrustDomain
