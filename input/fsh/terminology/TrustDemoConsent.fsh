// Draft consent codes of the demonstrator's trust domain: cross-border
// sharing of a child's immunization record and patient summary between
// Lao PDR and Thailand (owner, 2026-11-07: "New domain + codes"). Each
// definition is the text the person giving consent is shown. The terms-of-use
// ValueSet below is what a GDHCN TrustDomain record names
// (TrustDomain.termsOfUse in the GDHCN Trust IG); the proposed record is in
// docs/proposals/trust-domain/. Fictional demonstrator content.

CodeSystem: TrustDemoConsent
Id: TrustDemoConsent
Title: "Demonstrator trust domain: consent codes (draft)"
Description: "The consent policies of the demonstrator's draft trust domain for cross-border immunization records (Lao PDR and Thailand). Each code's definition is the consent text shown to the person who gives it."
* ^experimental = true
* ^caseSensitive = true
* ^status = #draft
* ^version = "0.1.0"
* #SHARE-SUMMARY-FOR-CARE "Share my child's summary for care across the border" "I agree that a health worker I give the QR code and the passcode to may read my child's patient summary to treat them, for the days I choose. I can stop it at any time in the family wallet."
* #SHARE-RECORD-WITH-HOME-CLINIC "Share my child's vaccinations with our home clinic" "I agree that vaccinations my child receives abroad may be sent to our home clinic and added to their record."

ValueSet: TrustDemoConsent
Id: TrustDemoConsent
Title: "Demonstrator trust domain: terms of use (draft)"
Description: "The terms-of-use ValueSet of the demonstrator's draft trust domain: the consent codes a consent names (R5 Consent.regulatoryBasis; R4 policyRule) and a VHL Receiver may name in a credential's termsOfUse."
* ^experimental = true
* ^status = #draft
* include codes from system TrustDemoConsent
