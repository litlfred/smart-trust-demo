The journeys do not restate requirements. Each step of a [user scenario](scenarios.html) names the requirement it exercises by its id (for example [STT-VER-011](https://litlfred.github.io/smart-trust-tools/viewers/requirements.html#stt-ver-011), read without verifying, in J2). Those requirements are defined, with their tests, on [smart-trust-tools' requirements page](https://litlfred.github.io/smart-trust-tools/viewers/requirements.html) (sources in [skills/requirements](https://github.com/litlfred/smart-trust-tools/tree/main/skills/requirements)), which traces them to [WHO SMART Trust](https://smart.who.int/trust) and [IHE ITI VHL](https://profiles.ihe.net/ITI/VHL/).

The WHO SMART Trust PHW requirements map onto the journeys as follows:

- `provide-a-vhl-to-a-receiver` (Holder): J2, J3 and J4.1.
- `receive-a-vhl` (Receiver): J2, J3 and J4.1.
- `publish-`, `receive-`, `distribute-` and `retrieve-pki-material`: the trust anchor and the participants, preconditions of J1, J3, J4.0 and J4.1.
