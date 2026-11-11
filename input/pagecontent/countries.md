The journeys take place in two fictional countries, so that no real country, ministry or signing key is implied. Each is defined once, in `scenarios/countries/`, with a code from the ISO 3166-1 alpha-3 user-assigned range (XAA to XZZ), which never names a real country. Other journeys, such as the pilgrimage, reuse the same two countries and codes.

| Country | Code | Role | Places | In these journeys |
|---|---|---|---|---|
| **Onesa** (adjective: Onesan) | XXK | home | Lomaru (capital), Village 04 | Country B: the family's home (J2, J3, J4.0), whose national portal serves their records abroad (J4.1) |
| **Taifafeki** (adjective: Taifafeki) | XXR | visited | Lumara (capital), Kesaro (border province) | Country A: where the newborn is born (J1) and later seen at the point of care (J4.1) |
{: .grid }

### Codes

Both codes are in the SMART Trust value set of GDHCN DEV participants, [Participants-DEV](http://smart.who.int/trust/ValueSet/Participants-DEV), whose code system names XXK "Onesa" and XXR "Taifafeki". Both are onboarded test participants of the GDHCN DEV network (WorldHealthOrganization/tng-participants-dev): XXR's document signer key signs the birth-dose DVCs of J1, and XXK plays Onesa's national portal in J4. Their keys are test keys, not any ministry's.

### Reuse

A journey that needs a home country and a visited country takes Onesa and Taifafeki from `scenarios/countries/onesa.json` and `scenarios/countries/taifafeki.json`: the name, adjective, code, role and places. The people in a journey are its own, and fictional too.
