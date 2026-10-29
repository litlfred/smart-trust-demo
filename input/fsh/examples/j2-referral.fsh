// J2: the CHW registers Chanthala and refers her to the home clinic. The
// foreign DVCs were read without verifying (read-unverified), so the referral
// says so: nothing on them is a verified record until J3.

Instance: TrustDemoJ2Referral
InstanceOf: ServiceRequest
Title: "J2 referral to the home clinic"
Description: "Sita RAI's referral of Chanthala to the district clinic after a home visit. The two foreign DVCs were read unverified on the CHW app, offline; the clinic is to verify them and give any dose due."
Usage: #example
* status = #active
* intent = #order
* code.concept = $sct#3457005 "Patient referral"
* subject = Reference(TrustDemoChanthala)
* authoredOn = "2026-11-02"
* requester = Reference(TrustDemoSitaRai)
* performer = Reference(TrustDemoHomeClinic)
* reason[+].concept.text = "Infant born abroad, not in the household register; presents two foreign paper DVCs (Hep B, BCG birth doses) read unverified"
* note.text = "The doses shown on the CHW app are unverified (triage read). Verify the DVCs against the trust list before importing them."
