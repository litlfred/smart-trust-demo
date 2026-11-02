// J3a and J3b, Vientiane District Health Center, Lao PDR, 2025-11-25 (T0 + 4
// weeks). Nurse Chanthasone scans the DVCs; the EHR verifies each against its
// cached GDHCN DEV trust list (XXR's DSC, kid 916ffa567c0f44a2), offline, and
// imports the doses with provenance. The issuer's product coding is kept and
// the national schedule coding is added beside it (ConceptMap; the nurse
// confirms the Hep B product, which had no mapping). The schedule then finds
// the 6-week doses due and books them.

Instance: TrustDemoJ3HepB
InstanceOf: TrustDemoLaoImmunization
Title: "J3 verified: Hep B birth dose (Thailand), with both codings"
Description: "The Hep B birth dose after the EHR verified its DVC: the verified DVC is the administering hospital's own signed record, so the dose is recorded from its primary source (the VaxLink trust ladder's 'verified' step). The issuer's product coding is kept, and the national schedule coding is added beside it."
Usage: #example
* status = #completed
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-hepb-peds-monovalent "Hepatitis B vaccine, paediatric, monovalent"
* vaccineCode.coding[laoEpi] = TrustDemoLaoEpiSchedule#LAO-EPI-HEPB-BD "Hepatitis B birth dose"
* vaccineCode.coding[cvx] = $cvx#08 "Hep B, adolescent or pediatric"
* vaccineCode.text = "Hepatitis B paediatric birth dose"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-10-28T09:15:00+07:00"
* primarySource = true
* informationSource.reference = Reference(TrustDemoChiangRaiHospital)
* performer.actor = Reference(TrustDemoSomchai)
* lotNumber = "TH-4821"
* location.display = "Chiang Rai Provincial Hospital, Thailand"
* protocolApplied.doseNumber = "1"

Instance: TrustDemoJ3Bcg
InstanceOf: TrustDemoLaoImmunization
Title: "J3 verified: BCG birth dose (Thailand), with both codings"
Description: "The BCG birth dose after the EHR verified its DVC, with the national schedule coding added beside the issuer's."
Usage: #example
* status = #completed
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-bcg-freeze-dried "BCG vaccine, freeze-dried"
* vaccineCode.coding[laoEpi] = TrustDemoLaoEpiSchedule#LAO-EPI-BCG "BCG"
* vaccineCode.coding[cvx] = $cvx#19 "BCG"
* vaccineCode.text = "BCG"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-10-28T09:20:00+07:00"
* primarySource = true
* informationSource.reference = Reference(TrustDemoChiangRaiHospital)
* performer.actor = Reference(TrustDemoSomchai)
* lotNumber = "TH-9012"
* location.display = "Chiang Rai Provincial Hospital, Thailand"
* protocolApplied.doseNumber = "1"

Instance: TrustDemoJ3Verification
InstanceOf: TrustDemoLaoDvcVerification
Title: "J3a provenance: DVCs verified against the GDHCN DEV trust list"
Description: "Records that the two doses come from DVCs the district EHR verified offline (COSE_Sign1, ES256) against XXR's DSC in its cached copy of the GDHCN DEV trust list, and that they replace the reported doses of J2."
Usage: #example
* target[+] = Reference(TrustDemoJ3HepB)
* target[+] = Reference(TrustDemoJ3Bcg)
* recorded = "2025-11-25T10:14:22+07:00"
* policy = "http://smart.who.int/trust"
* activity.text = "Verified each DVC (HCERT) offline against the cached GDHCN DEV trust list, then imported it"
* agent[+].type = http://terminology.hl7.org/CodeSystem/provenance-participant-type#verifier "Verifier"
* agent[=].who = Reference(TrustDemoDhcEhr)
* agent[+].type = http://terminology.hl7.org/CodeSystem/provenance-participant-type#enterer "Enterer"
* agent[=].who = Reference(TrustDemoChanthasone)
* agent[+].type = http://terminology.hl7.org/CodeSystem/provenance-participant-type#author "Author"
* agent[=].who = Reference(TrustDemoChiangRaiHospital)
* entity[+].role = #source
* entity[=].what.display = "DVC (HCERT, HC1 QR) for the Hep B birth dose, signed by XXR, kid 916ffa567c0f44a2"
* entity[+].role = #source
* entity[=].what.display = "DVC (HCERT, HC1 QR) for the BCG birth dose, signed by XXR, kid 916ffa567c0f44a2"
* entity[+].role = #removal
* entity[=].what = Reference(TrustDemoJ2HepBReported)
* entity[+].role = #removal
* entity[=].what = Reference(TrustDemoJ2BcgReported)

Instance: TrustDemoJ3Adjudication
InstanceOf: Provenance
Title: "J3b provenance: the nurse's vaccine-code adjudication"
Description: "Records Nurse Chanthasone's clinical call that the Thai Hep B product counts as the national Hep B birth dose, which the map did not yet cover. The decision is added to the national ConceptMap for the next clinic."
Usage: #example
* target[+] = Reference(TrustDemoJ3HepB)
* target[+] = Reference(TrustDemoProductToLaoEpi)
* recorded = "2025-11-25T10:21:00+07:00"
* activity.text = "Confirmed vp-hepb-peds-monovalent as equivalent to LAO-EPI-HEPB-BD; issuer coding kept, schedule coding added"
* agent[+].type = http://terminology.hl7.org/CodeSystem/provenance-participant-type#attester "Attester"
* agent[=].who = Reference(TrustDemoChanthasone)

Instance: TrustDemoJ3Recommendation
InstanceOf: ImmunizationRecommendation
Title: "J3b schedule evaluation: the 6-week doses are due"
Description: "The national schedule run over the verified doses read by their schedule codes: the Hep B and BCG birth doses count, and pentavalent 1, bOPV 1 and PCV 1 fall due at 6 weeks (2025-12-09)."
Usage: #example
* patient = Reference(TrustDemoSomsack)
* date = "2025-11-25T10:22:00+07:00"
* authority = Reference(TrustDemoVientianeDhc)
* recommendation[+].vaccineCode = TrustDemoLaoEpiSchedule#LAO-EPI-PENTA-1 "Pentavalent (DTP-HepB-Hib), dose 1"
* recommendation[=].forecastStatus = http://terminology.hl7.org/CodeSystem/immunization-recommendation-status#due "Due"
* recommendation[=].dateCriterion.code = $loinc#30980-7 "Date vaccine due"
* recommendation[=].dateCriterion.value = "2025-12-09"
* recommendation[=].supportingImmunization[+] = Reference(TrustDemoJ3HepB)
* recommendation[+].vaccineCode = TrustDemoLaoEpiSchedule#LAO-EPI-OPV-1 "bOPV, dose 1"
* recommendation[=].forecastStatus = http://terminology.hl7.org/CodeSystem/immunization-recommendation-status#due "Due"
* recommendation[=].dateCriterion.code = $loinc#30980-7 "Date vaccine due"
* recommendation[=].dateCriterion.value = "2025-12-09"
* recommendation[+].vaccineCode = TrustDemoLaoEpiSchedule#LAO-EPI-PCV-1 "PCV, dose 1"
* recommendation[=].forecastStatus = http://terminology.hl7.org/CodeSystem/immunization-recommendation-status#due "Due"
* recommendation[=].dateCriterion.code = $loinc#30980-7 "Date vaccine due"
* recommendation[=].dateCriterion.value = "2025-12-09"

Instance: TrustDemoJ3Reminder
InstanceOf: Task
Title: "J3b reminder: bring Somsack back for the 6-week doses"
Description: "The reminder the schedule evaluation creates, so Khamla leaves knowing exactly when to come back."
Usage: #example
* status = #requested
* intent = #plan
* code.text = "Immunization appointment reminder: 6-week doses"
* focus = Reference(TrustDemoJ3Recommendation)
* for = Reference(TrustDemoSomsack)
* authoredOn = "2025-11-25T10:22:00+07:00"
* requester = Reference(TrustDemoVientianeDhc)
* requestedPeriod.start = "2025-12-09"
* requestedPeriod.end = "2025-12-16"

// The doses Somsack is given in Lao PDR over his first year, recorded at the
// district health center (primary source).

Instance: TrustDemoLaoPenta1
InstanceOf: TrustDemoLaoImmunization
Title: "Lao dose: pentavalent 1 (2025-12-10)"
Description: "Given at Vientiane District Health Center at 6 weeks, as the J3 schedule booked it."
Usage: #example
* status = #completed
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-pentavalent-liquid "DTP-HepB-Hib (pentavalent), liquid"
* vaccineCode.coding[laoEpi] = TrustDemoLaoEpiSchedule#LAO-EPI-PENTA-1 "Pentavalent (DTP-HepB-Hib), dose 1"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-12-10"
* primarySource = true
* performer.actor = Reference(TrustDemoChanthasone)
* lotNumber = "LA-2201"
* location.display = "Vientiane District Health Center, Lao PDR"
* basedOn = Reference(TrustDemoJ3Recommendation)
* protocolApplied.doseNumber = "1"

Instance: TrustDemoLaoBopv1
InstanceOf: TrustDemoLaoImmunization
Title: "Lao dose: bOPV 1 (2025-12-10)"
Description: "Given at Vientiane District Health Center at 6 weeks."
Usage: #example
* status = #completed
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-bopv-drops "Bivalent oral polio vaccine (bOPV), drops"
* vaccineCode.coding[laoEpi] = TrustDemoLaoEpiSchedule#LAO-EPI-OPV-1 "bOPV, dose 1"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-12-10"
* primarySource = true
* performer.actor = Reference(TrustDemoChanthasone)
* lotNumber = "LA-5531"
* location.display = "Vientiane District Health Center, Lao PDR"
* basedOn = Reference(TrustDemoJ3Recommendation)
* protocolApplied.doseNumber = "1"

Instance: TrustDemoLaoPcv1
InstanceOf: TrustDemoLaoImmunization
Title: "Lao dose: PCV 1 (2025-12-10)"
Description: "Given at Vientiane District Health Center at 6 weeks."
Usage: #example
* status = #completed
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-pcv-13-dose "Pneumococcal conjugate vaccine (PCV)"
* vaccineCode.coding[laoEpi] = TrustDemoLaoEpiSchedule#LAO-EPI-PCV-1 "PCV, dose 1"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2025-12-10"
* primarySource = true
* performer.actor = Reference(TrustDemoChanthasone)
* lotNumber = "LA-8819"
* location.display = "Vientiane District Health Center, Lao PDR"
* basedOn = Reference(TrustDemoJ3Recommendation)
* protocolApplied.doseNumber = "1"

Instance: TrustDemoLaoMr1
InstanceOf: TrustDemoLaoImmunization
Title: "Lao dose: measles-rubella 1 (2026-07-28)"
Description: "Given at Vientiane District Health Center at 9 months."
Usage: #example
* status = #completed
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-mr-freeze-dried "Measles-rubella vaccine, freeze-dried"
* vaccineCode.coding[laoEpi] = TrustDemoLaoEpiSchedule#LAO-EPI-MR-1 "Measles-rubella, dose 1"
* patient = Reference(TrustDemoSomsack)
* occurrenceDateTime = "2026-07-28"
* primarySource = true
* performer.actor = Reference(TrustDemoChanthasone)
* lotNumber = "LA-9923"
* location.display = "Vientiane District Health Center, Lao PDR"
* protocolApplied.doseNumber = "1"
