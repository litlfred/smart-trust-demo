// J4.0: the national portal assembles Chanthala's IPS, which it encrypts
// behind her passcode-protected VHL; J4.1: the hospital abroad receives it.
// The Bundle follows the IPS document shape (Composition, LOINC 60591-5)
// without claiming the IPS profiles, which this guide does not depend on.

Instance: TrustDemoJ4Composition
InstanceOf: Composition
Title: "J4.0 Chanthala's patient summary (Composition)"
Description: "The patient summary the national portal of Country B assembles for Chanthala before the family travels."
Usage: #inline
* status = #final
* type = $loinc#60591-5 "Patient summary Document"
* subject = Reference(Patient/TrustDemoChanthala)
* date = "2026-11-20T10:00:00Z"
* author.display = "National health portal, Country B (XXH)"
* title = "Patient summary: Chanthala SOUVANNALATH"
* section[+].title = "Allergies and intolerances"
* section[=].code = $loinc#48765-2 "Allergies and adverse reactions Document"
* section[=].emptyReason = http://terminology.hl7.org/CodeSystem/list-empty-reason#unavailable "Unavailable"
* section[+].title = "Medication summary"
* section[=].code = $loinc#10160-0 "History of Medication use Narrative"
* section[=].emptyReason = http://terminology.hl7.org/CodeSystem/list-empty-reason#unavailable "Unavailable"
* section[+].title = "Problems"
* section[=].code = $loinc#11450-4 "Problem list - Reported"
* section[=].emptyReason = http://terminology.hl7.org/CodeSystem/list-empty-reason#unavailable "Unavailable"
* section[+].title = "Immunizations"
* section[=].code = $loinc#11369-6 "History of Immunization Narrative"
* section[=].entry[+] = Reference(Immunization/TrustDemoJ3HepBImported)
* section[=].entry[+] = Reference(Immunization/TrustDemoJ3BcgImported)
* section[=].entry[+] = Reference(Immunization/TrustDemoJ3Opv0)

Instance: TrustDemoJ4Ips
InstanceOf: Bundle
Title: "J4.0 Chanthala's IPS (document Bundle)"
Description: "The patient summary document the portal puts behind Chanthala's VHL in J4.0, and that the hospital abroad decrypts in J4.1: her three doses, two of them imported from verified DVCs."
Usage: #example
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:5f0c3a8e-2b1d-4c7e-9a64-1d2e3f4a5b6c"
* type = #document
* timestamp = "2026-11-20T10:00:00Z"
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Composition/TrustDemoJ4Composition"
* entry[=].resource = TrustDemoJ4Composition
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Patient/TrustDemoChanthala"
* entry[=].resource = TrustDemoChanthala
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3HepBImported"
* entry[=].resource = TrustDemoJ3HepBImported
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3BcgImported"
* entry[=].resource = TrustDemoJ3BcgImported
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3Opv0"
* entry[=].resource = TrustDemoJ3Opv0

Instance: TrustDemoJ41Received
InstanceOf: Provenance
Title: "J4.1 provenance of the records received abroad"
Description: "Records how the hospital system abroad obtained Chanthala's IPS: it verified the VHL's HCERT against Country B's DSC in its cached trust list, fetched the manifest by ITI-YY5 with HTTP Message Signatures, and decrypted the document with the passcode Mali gave."
Usage: #example
* target = Reference(TrustDemoJ4Ips)
* recorded = "2026-12-05T21:40:00Z"
* activity.text = "Verified the VHL (HCERT) offline, fetched the manifest (ITI-YY5), decrypted the IPS (JWE)"
* agent[+].who = Reference(TrustDemoPocReceiver)
* agent[+].who = Reference(TrustDemoAnaMoreira)
* agent[+].who = Reference(TrustDemoMali)
* agent[=].type.text = "Holder: showed the VHL QR and gave the passcode"
* entity[+].role = #source
* entity[=].what.display = "VHL for Chanthala (HCERT, VHL at key 5), issued by Country B (XXH)"
