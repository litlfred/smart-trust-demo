# Proposal: a trust domain for the demonstrator's cross-border immunization records

Status: **draft, for the owner** (owner, 2026-11-07: "New domain + codes").

The demonstrator's journeys share a child's immunization record and patient
summary between Lao PDR and Thailand under the holder's explicit consent. No
GDHCN trust domain covers this. DDCC's terms of use are obligations on
participants, not patient consent, and IPS-PILGRIMAGE is for Hajj. This
repository now holds the draft consent codes,
`input/fsh/terminology/TrustDemoConsent.fsh`. The trust domain record itself
belongs in the GDHCN Trust IG (litlfred/smart-trust), which this repository
does not change. Below is the record to propose there, in that IG's
`TrustDomain` logical model:

```fsh
Instance: TrustDomain-TRUST-DEMO
InstanceOf: TrustDomain
Title: "Trust Domain: cross-border immunization records (demonstrator, draft)"
Usage: #example
* code = #TRUST-DEMO
* name = "Cross-border immunization records (demonstrator)"
* description = "**Draft, fictional demonstrator.** A child's immunization record and patient summary shared between Lao PDR and Thailand with the holder's explicit consent, by verifiable health link."
* useCase[0].title = "Share a child's summary for care across the border"
* useCase[0].dakComponent[0].component = #user-scenarios
* useCase[0].dakComponent[0].reference = "http://smart.who.int/trust-demo/journeys.html"
* technicalSpecification[0] = "http://smart.who.int/trust-demo"
* technicalSpecification[1] = "http://smart.who.int/trust-phw"
* policyStandard[0].text = "Data is shared only with the holder's explicit consent (opt-in: the implied default is the IHE PCF implicit policy Policy-deny); the consent travels in the shared summary."
* termsOfUse.valueSet = "http://smart.who.int/trust-demo/ValueSet/TrustDemoConsent"
* termsOfUse.process[0] = "http://smart.who.int/trust-phw/business-processes.html"
```

The smart-trust `Domains` CodeSystem would also need the code `TRUST-DEMO`.
