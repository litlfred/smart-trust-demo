// J1, Kesaro Provincial Hospital, Taifafeki (Country A), 2025-10-28 (T0).
// Somsak is born; Dr Anan gives the Hep B and BCG birth doses; the
// hospital records them under its own hospital number and prints one signed
// DVC (HCERT, XXR's key, kid 916ffa567c0f44a2) per dose. These are the Taifafeki
// records behind those cards; the Onesan records of the same doses are in J2
// (reported) and J3 (verified).

Alias: $ThHn = http://smart.who.int/trust-demo/sid/xxr-kesaro-hn
Alias: $cvx = http://hl7.org/fhir/sid/cvx

Instance: TrustDemoTaifafekiSomsak
InstanceOf: TrustDemoTaifafekiPatient
Title: "Taifafeki: Somsak at the birth hospital (hospital number)"
Description: "Somsak as Kesaro Provincial Hospital registers him on the day he is born: a hospital number and no Taifafeki citizen id, since his parents are Onesan. The same child is TrustDemoSomsak in Onesa. Fictional."
Usage: #example
* identifier[hn].system = $ThHn
* identifier[hn].value = "CRH-HN-68-104377"
* name.use = #official
* name.family = "SENGMANY"
* name.given = "Somsak"
* gender = #male
* birthDate = "2025-10-28"
* managingOrganization = Reference(TrustDemoKesaroHospital)

Instance: TrustDemoJ1HepB
InstanceOf: TrustDemoTaifafekiImmunization
Title: "Taifafeki: Hep B birth dose, as the hospital records and signs it"
Description: "The record behind the first DVC Khamla carries home: product, date, lot, dose number and performer, the fields the HCERT certificate carries."
Usage: #example
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-hepb-peds-monovalent "Hepatitis B vaccine, paediatric, monovalent"
* vaccineCode.coding[cvx] = $cvx#08 "Hep B, adolescent or pediatric"
* patient = Reference(TrustDemoTaifafekiSomsak)
* occurrenceDateTime = "2025-10-28T09:15:00+07:00"
* performer.actor = Reference(TrustDemoAnan)
* lotNumber = "XXR-4821"
* location.display = "Kesaro Provincial Hospital, Taifafeki"
* protocolApplied.doseNumberPositiveInt = 1

Instance: TrustDemoJ1Bcg
InstanceOf: TrustDemoTaifafekiImmunization
Title: "Taifafeki: BCG birth dose, as the hospital records and signs it"
Description: "The record behind the second DVC: the BCG birth dose."
Usage: #example
* vaccineCode.coding[product] = TrustDemoVaccineProduct#vp-bcg-freeze-dried "BCG vaccine, freeze-dried"
* patient = Reference(TrustDemoTaifafekiSomsak)
* occurrenceDateTime = "2025-10-28T09:20:00+07:00"
* performer.actor = Reference(TrustDemoAnan)
* lotNumber = "XXR-9012"
* location.display = "Kesaro Provincial Hospital, Taifafeki"
* protocolApplied.doseNumberPositiveInt = 1
