// J4.0 and J4.1, 12 months on. The family plans a trip to Taifafeki. On
// Bounmy's phone, the family wallet holds a profile for each of them; for
// Somsak he shares a passcode-protected VHL valid for 14 days (J4.0). At a
// primary care clinic in Kesaro, Dr Anan scans it, Bounmy says the
// passcode, and the viewer fetches Somsak's IPS from Onesa; the Onesan gateway
// logs the access at home (J4.1). The Bundle follows the IPS document shape
// (Composition, LOINC 60591-5) and carries the consent it is shared under
// (an Advance Directives section and a Consent entry), without claiming the IPS profiles, which this
// guide does not depend on.

Instance: TrustDemoJ4Composition
InstanceOf: Composition
Title: "J4.0 Somsak's patient summary (Composition)"
Description: "The patient summary the Onesan portal assembles for Somsak before the trip: six doses, two from Taifafeki (verified in J3) and four given in Onesa."
Usage: #example
* status = #final
* type = $loinc#60591-5 "Patient summary Document"
* subject = Reference(Patient/TrustDemoSomsak)
* date = "2026-10-26T09:00:00+07:00"
* author.display = "Onesa national health portal (Country B, XXK)"
* title = "Patient summary: Somsak SENGMANY"
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
* section[=].entry[+] = Reference(Immunization/TrustDemoOnesaPenta1)
* section[=].entry[+] = Reference(Immunization/TrustDemoOnesaBopv1)
* section[=].entry[+] = Reference(Immunization/TrustDemoOnesaPcv1)
* section[=].entry[+] = Reference(Immunization/TrustDemoOnesaMr1)
* section[+].title = "Advance directives: consent"
* section[=].code = $loinc#42348-3 "Advance directives"
* section[=].text.status = #generated
* section[=].text.div = "<div xmlns=\"http://www.w3.org/1999/xhtml\">Shared with Bounmy's consent: anyone he gives the QR code and the spoken passcode to may read this summary for treatment, from 26 October to 9 November 2026.</div>"
* section[=].entry[+] = Reference(Consent/TrustDemoJ4Consent)

Instance: TrustDemoJ4Ips
InstanceOf: Bundle
Title: "J4.0 Somsak's IPS (document Bundle)"
Description: "The patient summary document behind Somsak's VHL: encrypted by the Onesan portal in J4.0, decrypted by the Kesaro clinic viewer in J4.1. Six doses, two of them from Taifafeki with their original coding kept."
Usage: #example
* identifier.system = "urn:ietf:rfc:3986"
* identifier.value = "urn:uuid:8d3f1c52-6a4e-4b0f-9c1d-2e7a5b9f0c31"
* type = #document
* timestamp = "2026-10-26T09:00:00+07:00"
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Composition/TrustDemoJ4Composition"
* entry[=].resource = TrustDemoJ4Composition
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Patient/TrustDemoSomsak"
* entry[=].resource = TrustDemoSomsak
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3HepB"
* entry[=].resource = TrustDemoJ3HepB
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoJ3Bcg"
* entry[=].resource = TrustDemoJ3Bcg
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoOnesaPenta1"
* entry[=].resource = TrustDemoOnesaPenta1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoOnesaBopv1"
* entry[=].resource = TrustDemoOnesaBopv1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoOnesaPcv1"
* entry[=].resource = TrustDemoOnesaPcv1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Immunization/TrustDemoOnesaMr1"
* entry[=].resource = TrustDemoOnesaMr1
* entry[+].fullUrl = "http://smart.who.int/trust-demo/Consent/TrustDemoJ4Consent"
* entry[=].resource = TrustDemoJ4Consent

Instance: TrustDemoJ4Consent
InstanceOf: PHWExplicitConsent
Title: "J4.0b Bounmy's consent to share Somsak's summary for 14 days"
Description: "Recorded when Bounmy creates Somsak's VHL (IHE Privacy Consent on FHIR): anyone he gives the QR and the spoken passcode to may read the summary for treatment, for 14 days. The passcode itself is never stored in the record. An explicit consent in the sense of the Personal Health Wallet guide (http://smart.who.int/trust-phw/consent.html): an opt-in (HL7 ActConsentDirective OPTIN) that adds this permission to the opt-in default, the IHE PCF implicit policy Policy-deny, with Bounmy's own act on the family wallet as the evidence. Consent.policyRule names the consent he agreed to, CONSENT-VHL-TREATMENT of the DEMO-VHL trust domain's terms of use (TrustDemoVhlTermsOfUse), with the version of its text he was shown. The IPS carries it as a consent entry, listed in its Advance Directives section; the copy in the IPS is evidence for the clinic, and the Onesan portal enforces the copy in its own record."
Usage: #example
* status = #active
* scope = http://terminology.hl7.org/CodeSystem/consentscope#patient-privacy "Privacy Consent"
* category[+] = $loinc#59284-0 "Consent Document"
* category[+] = http://terminology.hl7.org/CodeSystem/v3-ActCode#OPTIN "opt-in"
* patient = Reference(TrustDemoSomsak)
* dateTime = "2026-10-26"
* performer = Reference(TrustDemoBounmy)
* organization = Reference(TrustDemoOnesaPortalOrg)
* sourceAttachment.contentType = #application/json
* sourceAttachment.title = "Bounmy's confirmation on the family wallet when he created Somsak's VHL (explicit consent)"
* policyRule = TrustDemoVhlConsent|0.1.0#CONSENT-VHL-TREATMENT "Consent to read the summary for treatment"
* provision.type = #permit
* provision.period.start = "2026-10-26"
* provision.period.end = "2026-11-09"
* provision.purpose = http://terminology.hl7.org/CodeSystem/v3-ActReason#TREAT "treatment"
* provision.data[iData].meaning = #instance
* provision.data[iData].reference = Reference(TrustDemoJ4Ips)

Instance: TrustDemoJ41Received
InstanceOf: TrustDemoTaifafekiVhlReceipt
Title: "J4.1 provenance of the summary viewed in Kesaro"
Description: "How the Kesaro clinic viewer obtained Somsak's IPS: it verified the VHL's HCERT against Country B's DSC in its cached trust list, fetched the manifest by ITI-YY5 with an HTTP Message Signature once Bounmy said the passcode, and decrypted the document. Viewed, not copied into a Taifafeki registry."
Usage: #example
* target = Reference(TrustDemoJ4Ips)
* recorded = "2026-10-28T14:30:20+07:00"
* activity.text = "Verified the VHL (HCERT) offline, fetched the manifest (ITI-YY5), decrypted the IPS (JWE)"
* agent[+].who = Reference(TrustDemoClinicViewer)
* agent[+].who = Reference(TrustDemoAnan)
* agent[+].who = Reference(TrustDemoBounmy)
* agent[=].type.text = "Holder: showed the VHL QR and said the passcode"
* entity[+].role = #source
* entity[=].what.display = "VHL for Somsak (HCERT, VHL at key 5), issued by Country B (XXK)"
* entity[+].role = #source
* entity[=].what = Reference(TrustDemoJ4Consent)

Instance: TrustDemoJ41Access
InstanceOf: TrustDemoOnesaVhlAccess
Title: "J4.1 access logged in Onesa: manifest released"
Description: "The record the Onesan gateway keeps when the Kesaro clinic viewer retrieves Somsak's VHL manifest with the right passcode (IHE Basic Audit Log Patterns): who looked, from where, and when."
Usage: #example
* type = http://dicom.nema.org/resources/ontology/DCM#110112 "Query"
* subtype.display = "IHE ITI VHL manifest retrieval (ITI-YY5)"
* action = #E
* recorded = "2026-10-28T14:30:15+07:00"
* outcome = #0
* outcomeDesc = "Passcode verified; manifest released to the receiver"
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#IRCP "information recipient"
* agent[=].who = Reference(TrustDemoClinicViewer)
* agent[=].requestor = true
* agent[=].network.address = "clinic-viewer.kesaro.example"
* agent[=].network.type = #1
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#CST "custodian"
* agent[=].who = Reference(TrustDemoOnesaGateway)
* agent[=].requestor = false
* source.observer = Reference(TrustDemoOnesaGateway)
* entity[+].what = Reference(TrustDemoSomsak)
* entity[=].role = http://terminology.hl7.org/CodeSystem/object-role#1 "Patient"
* entity[+].what = Reference(TrustDemoJ4Consent)
* entity[+].what = Reference(TrustDemoJ4Ips)

Instance: TrustDemoJ41WrongPasscode
InstanceOf: TrustDemoOnesaVhlAccess
Title: "J4.1 wrong passcode: refused, and still logged in Onesa"
Description: "The 'what if' of J4.1: a manifest request with the wrong passcode is refused, and the attempt is logged at home all the same."
Usage: #example
* type = http://dicom.nema.org/resources/ontology/DCM#110112 "Query"
* subtype.display = "IHE ITI VHL manifest retrieval (ITI-YY5)"
* action = #E
* recorded = "2026-10-28T14:29:02+07:00"
* outcome = #4
* outcomeDesc = "Wrong passcode; manifest not released"
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#IRCP "information recipient"
* agent[=].who = Reference(TrustDemoClinicViewer)
* agent[=].requestor = true
* agent[=].network.address = "clinic-viewer.kesaro.example"
* agent[=].network.type = #1
* agent[+].type = http://terminology.hl7.org/CodeSystem/v3-ParticipationType#CST "custodian"
* agent[=].who = Reference(TrustDemoOnesaGateway)
* agent[=].requestor = false
* source.observer = Reference(TrustDemoOnesaGateway)
* entity[+].what = Reference(TrustDemoSomsak)
* entity[=].role = http://terminology.hl7.org/CodeSystem/object-role#1 "Patient"
