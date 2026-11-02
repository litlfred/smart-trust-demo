// Country A, Thailand: what the birth hospital records (J1) and what the
// point-of-care clinic keeps when it reads a family's VHL a year later (J4.1).
// Thailand is played on the GDHCN DEV network by test participant XXR.
// Demonstrator profiles: they show which elements each step relies on, not
// any real Thai national specification.

Alias: $ThHn = http://smart.who.int/trust-demo/sid/th-chiang-rai-hn

Profile: TrustDemoThPatient
Parent: Patient
Id: TrustDemoThPatient
Title: "Thailand: newborn at the birth hospital"
Description: """
How it is used: J1. Chiang Rai Provincial Hospital registers Somsack under its own hospital number on the day he is born.

Why: a baby born to Lao parents in Thailand has no Thai citizen id, so the hospital number is the only identifier the hospital can put behind the dose records it signs. The DVCs it prints carry the name and date of birth, not this number. The family's home country therefore cannot rely on any Thai identifier, and links the doses to its own patient (see the Lao patient profile).
"""
* identifier 1..* MS
* identifier ^slicing.discriminator.type = #value
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
* identifier contains hn 1..1 MS
* identifier[hn].system = $ThHn
* identifier[hn].value 1..1
* name 1..* MS
* birthDate 1..1 MS
* gender MS

Profile: TrustDemoThImmunization
Parent: Immunization
Id: TrustDemoThImmunization
Title: "Thailand: dose given at the birth hospital (DVC source)"
Description: """
How it is used: J1. Each birth dose (Hep B, BCG) that Dr Anan gives is recorded here first. The hospital then packs it into a Digital Vaccination Certificate (HCERT, signed with XXR's key) and prints it as a QR card.

Why: the DVC can only carry what this record holds. The vaccine product, date, lot, dose number and the administering organization are exactly the fields the HCERT certificate needs. They are required here so every printed card is complete. The product is coded from the WHO PreQual-style product list, because that is the code Lao PDR will later map to its own schedule (J3).
"""
* status = #completed
* vaccineCode.coding ^slicing.discriminator.type = #value
* vaccineCode.coding ^slicing.discriminator.path = "system"
* vaccineCode.coding ^slicing.rules = #open
* vaccineCode.coding contains product 1..1 MS and cvx 0..1
* vaccineCode.coding[cvx].system = "http://hl7.org/fhir/sid/cvx"
* vaccineCode.coding[product] from TrustDemoVaccineProducts (required)
* vaccineCode.coding[product].system = Canonical(TrustDemoVaccineProduct)
* patient only Reference(TrustDemoThPatient)
* occurrence[x] only dateTime
* primarySource = true
* performer 1..* MS
* lotNumber 1..1 MS
* protocolApplied 1..* MS
* protocolApplied.doseNumber 1..1

Profile: TrustDemoThVhlReceipt
Parent: Provenance
Id: TrustDemoThVhlReceipt
Title: "Thailand: record of a summary read through a VHL"
Description: """
How it is used: J4.1. The Chiang Rai clinic viewer keeps this record when it opens Somsack's patient summary through the Verifiable Health Link that his father shows.

Why: the Thai clinic views the Lao record and does not copy it into a Thai registry. So the clinic keeps a note of what it saw, where it came from, and how it was verified: the VHL's signature against Lao PDR's key on the GDHCN trust list, the manifest fetch, and the passcode. The Lao side keeps its own log of the same access (the Lao audit profile).
"""
* target 1..* MS
* recorded MS
* activity 1..1 MS
* agent 2..* MS
* entity 1..* MS
