// J4.0 and J4.1, 12 months on. The family plans a trip to Thailand. On
// Bounmy's phone, the family wallet holds a profile for each of them; for
// Somsack he shares a passcode-protected VHL valid for 14 days (J4.0). At a
// primary care clinic in Chiang Rai, Dr Anan scans it, Bounmy says the
// passcode, and the viewer fetches Somsack's IPS from Lao PDR; the Lao gateway
// logs the access at home (J4.1). The Bundle follows the IPS document shape
// (Composition, LOINC 60591-5) and carries the consent it is shared under
// (an Advance Directives section and a Consent entry), without claiming the IPS profiles, which this
// guide does not depend on.

Instance: TrustDemoJ4Composition
InstanceOf: Composition
Title: "J4.0 Somsack's patient summary (Composition)"
Description: "The patient summary the Lao portal assembles for Somsack before the trip: six doses, two from Thailand (verified in J3) and four given in Lao PDR."
Usage: #example
* status = #final
* type = $loinc#60591-5 "Patient summary Document"
* subject = Reference(Patient/TrustDemoSomsack)
* date = "2026-10-26T09:00:00+07:00"
* author.display = "Lao PDR national health portal (Country B, XXH)"
* title = "Patient summary: Somsack SENGMANY"
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
* section[=].entry[+] = Reference(Immunization/TrustDemoJ3HepB)
* section[=].entry[+] = Reference(Immunization/TrustDemoJ3Bcg)
* section[=].entry[+] = Reference(Immunization/TrustDemoLaoPenta1)
* section[=].entry[+] = Reference(Immunization/TrustDemoLaoBopv1)
* section[=].entry[+] = Reference(Immunization/TrustDemoLaoPcv1)
* section[=].entry[+] = Reference(Immunization/TrustDemoLaoMr1)
* section[+].title = "Advance directives: consent"
* section[=].code = $loinc#42348-3 "Advance directives"
* section[=].text.status = #generated
* section[=].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\">Shared with Bounmy's consent: anyone he gives the QR code and the spoken passcode to may read this summary for treatment, from 26 October to 9 November 2026.</div>"
* section[=].entry[+] = Reference(Consent/TrustDemoJ4Consent)

Instance: TrustDemoJ4Ips
InstanceOf: Bundle
Title: "J4.0 Somsack's IPS (document Bundle)"
Description: "The patient summary document behind Somsack's VHL: encrypted by the Lao portal in J4.0, decrypted by the Chiang Rai clinic viewer in J4.1. Six doses, two of them from Thailand with their original coding kept."
Usage: #example
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:8d3f1c52-6a4e-4b0f-9c1d-2e7a5b9f0c31"
* type = #document
* timestamp = "2026-10-26T09:00:00+07:00"
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Composition/TrustDemoJ4Composition"
* entry[=].resource = TrustDemoJ4Composition
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Patient/TrustDemoSomsack"
* entry[=].resource = TrustDemoSomsack
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3HepB"
* entry[=].resource = TrustDemoJ3HepB
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3Bcg"
* entry[=].resource = TrustDemoJ3Bcg
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoLaoPenta1"
* entry[=].resource = TrustDemoLaoPenta1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoLaoBopv1"
* entry[=].resource = TrustDemoLaoBopv1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoLaoPcv1"
* entry[=].resource = TrustDemoLaoPcv1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoLaoMr1"
* entry[=].resource = TrustDemoLaoMr1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Consent/TrustDemoJ4Consent"
* entry[=].resource = TrustDemoJ4Consent

Instance: TrustDemoJ4Consent
InstanceOf: Consent
Title: "J4.0b Bounmy's consent to share Somsack's summary for 14 days"
Description: "Recorded when Bounmy creates Somsack's VHL (IHE Privacy Consent on FHIR): anyone he gives the QR and the spoken passcode to may read the summary for treatment, for 14 days. The passcode itself is never stored in the record. An explicit consent in the sense of the Personal Health Wallet guide (http://smart.who.int/trust-phw/consent.html): Bounmy's own act on the family wallet is the evidence. The IPS carries it as a consent entry, listed in its Advance Directives section; the copy in the IPS is evidence for the clinic, and the Lao portal enforces the copy in its own record."
Usage: #example
* status = #active
* category = $loinc#59284-0 "Consent Document"
* subject = Reference(TrustDemoSomsack)
* date = "2026-10-26"
* period.start = "2026-10-26"
* period.end = "2026-11-09"
* grantor = Reference(TrustDemoBounmy)
* controller = Reference(TrustDemoLaoPortalOrg)
* sourceAttachment.contentType = #application/json
* sourceAttachment.title = "Bounmy's confirmation on the family wallet when he created Somsack's VHL (explicit consent)"
* regulatoryBasis = TrustDemoConsent#SHARE-SUMMARY-FOR-CARE "Share my child's summary for care across the border"
* regulatoryBasis.coding.version = "0.1.0"
* decision = #permit
* provision.period.start = "2026-10-26"
* provision.period.end = "2026-11-09"
* provision.action = http://terminology.hl7.org/CodeSystem/consentaction#access "Access"
* provision.purpose = http://terminology.hl7.org/CodeSystem/v3-ActReason#TREAT "treatment"
* provision.data[+].meaning = #instance
* provision.data[=].reference = Reference(TrustDemoJ4Ips)

Instance: TrustDemoJ41Received
InstanceOf: TrustDemoThVhlReceipt
Title: "J4.1 provenance of the summary viewed in Chiang Rai"
Description: "How the Chiang Rai clinic viewer obtained Somsack's IPS: it verified the VHL's HCERT against Country B's DSC in its cached trust list, fetched the manifest by ITI-YY5 with an HTTP Message Signature once Bounmy said the passcode, and decrypted the document. Viewed, not copied into a Thai registry."
Usage: #example
* target = Reference(TrustDemoJ4Ips)
* recorded = "2026-10-28T14:30:20+07:00"
* activity.text = "Verified the VHL (HCERT) offline, fetched the manifest (ITI-YY5), decrypted the IPS (JWE)"
* agent[+].who = Reference(TrustDemoClinicViewer)
* agent[+].who = Reference(TrustDemoAnan)
* agent[+].who = Reference(TrustDemoBounmy)
* agent[=].type.text = "Holder: showed the VHL QR and said the passcode"
* entity[+].role = #source
* entity[=].what.display = "VHL for Somsack (HCERT, VHL at key 5), issued by Country B (XXH)"
* entity[+].role = #source
* entity[=].what = Reference(TrustDemoJ4Consent)

Instance: TrustDemoJ41Access
InstanceOf: TrustDemoLaoVhlAccess
Title: "J4.1 access logged in Lao PDR: manifest released"
Description: "The record the Lao gateway keeps when the Chiang Rai clinic viewer retrieves Somsack's VHL manifest with the right passcode (IHE Basic Audit Log Patterns): who looked, from where, and when."
Usage: #example
* category = http://dicom.nema.org/resources/ontology/DCM#110112 "Query"
* code.text = "IHE ITI VHL manifest retrieval (ITI-YY5)"
* action = #E
* recorded = "2026-10-28T14:30:15+07:00"
* outcome.code = http://terminology.hl7.org/CodeSystem/audit-event-outcome#0 "Success"
* outcome.detail.text = "Passcode verified; manifest released to the receiver"
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#IRCP "information recipient"
* agent[=].who = Reference(TrustDemoClinicViewer)
* agent[=].requestor = true
* agent[=].networkString = "clinic-viewer.chiang-rai.example"
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#CST "custodian"
* agent[=].who = Reference(TrustDemoLaoGateway)
* agent[=].requestor = false
* source.observer = Reference(TrustDemoLaoGateway)
* entity[+].what = Reference(TrustDemoSomsack)
* entity[=].role = http://terminology.hl7.org/CodeSystem/object-role#1 "Patient"
* entity[+].what = Reference(TrustDemoJ4Consent)
* entity[+].what = Reference(TrustDemoJ4Ips)

Instance: TrustDemoJ41WrongPasscode
InstanceOf: TrustDemoLaoVhlAccess
Title: "J4.1 wrong passcode: refused, and still logged in Lao PDR"
Description: "The 'what if' of J4.1: a manifest request with the wrong passcode is refused, and the attempt is logged at home all the same."
Usage: #example
* category = http://dicom.nema.org/resources/ontology/DCM#110112 "Query"
* code.text = "IHE ITI VHL manifest retrieval (ITI-YY5)"
* action = #E
* recorded = "2026-10-28T14:29:02+07:00"
* outcome.code = http://terminology.hl7.org/CodeSystem/audit-event-outcome#4 "Minor failure"
* outcome.detail.text = "Wrong passcode; manifest not released"
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#IRCP "information recipient"
* agent[=].who = Reference(TrustDemoClinicViewer)
* agent[=].requestor = true
* agent[=].networkString = "clinic-viewer.chiang-rai.example"
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#CST "custodian"
* agent[=].who = Reference(TrustDemoLaoGateway)
* agent[=].requestor = false
* source.observer = Reference(TrustDemoLaoGateway)
* entity[+].what = Reference(TrustDemoSomsack)
* entity[=].role = http://terminology.hl7.org/CodeSystem/object-role#1 "Patient"
