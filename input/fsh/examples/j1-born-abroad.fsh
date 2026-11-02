// J1, Chiang Rai Provincial Hospital, Thailand (Country A), 2025-10-28 (T0).
// Somsack is born; Dr Somchai gives the Hep B and BCG birth doses; the
// hospital records them under its own hospital number and prints one signed
// DVC (HCERT, XXR's key, kid 916ffa567c0f44a2) per dose. These are the Thai
// records behind those cards; the Lao records of the same doses are in J2
// (reported) and J3 (verified).

Alias: $ThHn = http://smart.who.int/trust-demo/sid/th-chiang-rai-hn
Alias: $cvx = http://hl7.org/fhir/sid/cvx

Instance: TrustDemoThSomsack
InstanceOf: TrustDemoThPatient
Title: "Thailand: Somsack at the birth hospital (hospital number)"
Description: "Somsack as Chiang Rai Provincial Hospital registers him on the day he is born: a hospital number and no Thai citizen id, since his parents are Lao. The same child is TrustDemoSomsack in Lao PDR. Fictional."
Usage: #example
* identifier[hn].system = $ThHn
* identifier[hn].value = "CRH-HN-68-104377"
* name.use = #official
* name.family = "SENGMANY"
* name.given = "Somsack"
* gender = #male
* birthDate = "2025-10-28"
* managingOrganization = Reference(TrustDemoChiangRaiHospital)

Instance: TrustDemoJ1HepB
InstanceOf: TrustDemoThImmunization
Title: "Thailand: Hep B birth dose, as the hospital records and signs it"
Description: "The record behind the first DVC Khamla carries home: product, date, lot, dose number and performer, the fields the HCERT certificate carries."
Usage: #example
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-hepb-peds-monovalent "Hepatitis B vaccine, paediatric, monovalent"
* vaccineCode.coding[cvx] = $cvx#08 "Hep B, adolescent or pediatric"
* patient = Reference(TrustDemoThSomsack)
* occurrenceDateTime = "2025-10-28T09:15:00+07:00"
* performer.actor = Reference(TrustDemoSomchai)
* lotNumber = "TH-4821"
* location.display = "Chiang Rai Provincial Hospital, Thailand"
* protocolApplied.doseNumber = "1"

Instance: TrustDemoJ1Bcg
InstanceOf: TrustDemoThImmunization
Title: "Thailand: BCG birth dose, as the hospital records and signs it"
Description: "The record behind the second DVC: the BCG birth dose."
Usage: #example
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-bcg-freeze-dried "BCG vaccine, freeze-dried"
* patient = Reference(TrustDemoThSomsack)
* occurrenceDateTime = "2025-10-28T09:20:00+07:00"
* performer.actor = Reference(TrustDemoSomchai)
* lotNumber = "TH-9012"
* location.display = "Chiang Rai Provincial Hospital, Thailand"
* protocolApplied.doseNumber = "1"
