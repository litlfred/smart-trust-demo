// French (fr) designations for this guide's own CodeSystems, as CodeSystem
// supplements (one file per locale). Agent translation, UNOFFICIAL: no human
// has reviewed or signed it off. Codes are unchanged; only displays,
// definitions and fr designations are given.

CodeSystem: TrustDemoVaccineProductFr
Id: TrustDemoVaccineProduct-fr
Title: "Produits vaccinaux (codes illustratifs de type PreQual)"
Description: "French (fr) supplement to TrustDemoVaccineProduct: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVaccineProduct)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 6
* #vp-hepb-peds-monovalent "Vaccin contre l'hépatite B, pédiatrique, monovalent"
* #vp-hepb-peds-monovalent ^designation[0].language = #fr
* #vp-hepb-peds-monovalent ^designation[0].value = "Vaccin contre l'hépatite B, pédiatrique, monovalent"
* #vp-bcg-freeze-dried "Vaccin BCG, lyophilisé"
* #vp-bcg-freeze-dried ^designation[0].language = #fr
* #vp-bcg-freeze-dried ^designation[0].value = "Vaccin BCG, lyophilisé"
* #vp-pentavalent-liquid "DTC-HepB-Hib (pentavalent), liquide"
* #vp-pentavalent-liquid ^designation[0].language = #fr
* #vp-pentavalent-liquid ^designation[0].value = "DTC-HepB-Hib (pentavalent), liquide"
* #vp-bopv-drops "Vaccin antipoliomyélitique oral bivalent (VPOb), gouttes"
* #vp-bopv-drops ^designation[0].language = #fr
* #vp-bopv-drops ^designation[0].value = "Vaccin antipoliomyélitique oral bivalent (VPOb), gouttes"
* #vp-pcv-13-dose "Vaccin antipneumococcique conjugué (VPC)"
* #vp-pcv-13-dose ^designation[0].language = #fr
* #vp-pcv-13-dose ^designation[0].value = "Vaccin antipneumococcique conjugué (VPC)"
* #vp-mr-freeze-dried "Vaccin contre la rougeole et la rubéole, lyophilisé"
* #vp-mr-freeze-dried ^designation[0].language = #fr
* #vp-mr-freeze-dried ^designation[0].value = "Vaccin contre la rougeole et la rubéole, lyophilisé"

CodeSystem: TrustDemoOnesaEpiScheduleFr
Id: TrustDemoOnesaEpiSchedule-fr
Title: "Codes antigène-dose du calendrier national (illustratifs, Onesa)"
Description: "French (fr) supplement to TrustDemoOnesaEpiSchedule: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoOnesaEpiSchedule)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 6
* #XXK-EPI-HEPB-BD "Dose à la naissance contre l'hépatite B"
* #XXK-EPI-HEPB-BD ^designation[0].language = #fr
* #XXK-EPI-HEPB-BD ^designation[0].value = "Dose à la naissance contre l'hépatite B"
* #XXK-EPI-BCG "BCG"
* #XXK-EPI-BCG ^designation[0].language = #fr
* #XXK-EPI-BCG ^designation[0].value = "BCG"
* #XXK-EPI-PENTA-1 "Pentavalent (DTC-HepB-Hib), dose 1"
* #XXK-EPI-PENTA-1 ^designation[0].language = #fr
* #XXK-EPI-PENTA-1 ^designation[0].value = "Pentavalent (DTC-HepB-Hib), dose 1"
* #XXK-EPI-OPV-1 "VPOb, dose 1"
* #XXK-EPI-OPV-1 ^designation[0].language = #fr
* #XXK-EPI-OPV-1 ^designation[0].value = "VPOb, dose 1"
* #XXK-EPI-PCV-1 "VPC, dose 1"
* #XXK-EPI-PCV-1 ^designation[0].language = #fr
* #XXK-EPI-PCV-1 ^designation[0].value = "VPC, dose 1"
* #XXK-EPI-MR-1 "Rougeole-rubéole, dose 1"
* #XXK-EPI-MR-1 ^designation[0].language = #fr
* #XXK-EPI-MR-1 ^designation[0].value = "Rougeole-rubéole, dose 1"

CodeSystem: TrustDemoDataElementsFr
Id: TrustDemoDataElements-fr
Title: "Éléments de données des parcours"
Description: "French (fr) supplement to TrustDemoDataElements: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoDataElements)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 77
* #TD.J1.DE01 "Nom" "Le nom de l'enfant tel que l'hôpital de naissance l'enregistre."
* #TD.J1.DE01 ^designation[0].language = #fr
* #TD.J1.DE01 ^designation[0].value = "Nom"
* #TD.J1.DE02 "Date de naissance" "La date de naissance de l'enfant."
* #TD.J1.DE02 ^designation[0].language = #fr
* #TD.J1.DE02 ^designation[0].value = "Date de naissance"
* #TD.J1.DE03 "Nom du parent ou tuteur" "Le parent ou tuteur, pour un sujet sans pièce d'identité, tel qu'un nouveau-né (STT-PAY-005)."
* #TD.J1.DE03 ^designation[0].language = #fr
* #TD.J1.DE03 ^designation[0].value = "Nom du parent ou tuteur"
* #TD.J1.DE04 "Numéro d'hôpital" "L'identifiant propre de l'enfant à l'hôpital de naissance. Il n'est pas porté dans le DVC."
* #TD.J1.DE04 ^designation[0].language = #fr
* #TD.J1.DE04 ^designation[0].value = "Numéro d'hôpital"
* #TD.J1.DE05 "Produit vaccinal" "Le produit administré, dans le codage des produits de l'émetteur (codes illustratifs de type PreQual)."
* #TD.J1.DE05 ^designation[0].language = #fr
* #TD.J1.DE05 ^designation[0].value = "Produit vaccinal"
* #TD.J1.DE06 "Date de vaccination" "La date d'administration de la dose. Le dossier hospitalier contient aussi l'heure ; le DVC porte la date."
* #TD.J1.DE06 ^designation[0].language = #fr
* #TD.J1.DE06 ^designation[0].value = "Date de vaccination"
* #TD.J1.DE07 "Numéro de lot" "Le lot du vaccin administré."
* #TD.J1.DE07 ^designation[0].language = #fr
* #TD.J1.DE07 ^designation[0].value = "Numéro de lot"
* #TD.J1.DE08 "Numéro de dose" "Le numéro de la dose dans sa série. Enregistré par l'hôpital ; la charge utile minimale du DVC ne le porte pas."
* #TD.J1.DE08 ^designation[0].language = #fr
* #TD.J1.DE08 ^designation[0].value = "Numéro de dose"
* #TD.J1.DE09 "Clinicien superviseur" "Le clinicien qui a administré ou supervisé la dose."
* #TD.J1.DE09 ^designation[0].language = #fr
* #TD.J1.DE09 ^designation[0].value = "Clinicien superviseur"
* #TD.J1.DE10 "Pays émetteur" "Le participant du réseau de confiance dont la clé signe le DVC (J1 : XXR)."
* #TD.J1.DE10 ^designation[0].language = #fr
* #TD.J1.DE10 ^designation[0].value = "Pays émetteur"
* #TD.J1.DE11 "Émis le" "Le moment où le DVC a été signé."
* #TD.J1.DE11 ^designation[0].language = #fr
* #TD.J1.DE11 ^designation[0].value = "Émis le"
* #TD.J1.DE12 "Expire le" "Le moment où le DVC cesse d'être vérifiable, lorsque l'émetteur fixe une expiration."
* #TD.J1.DE12 ^designation[0].language = #fr
* #TD.J1.DE12 ^designation[0].value = "Expire le"
* #TD.J1.DE13 "Identifiant de clé (kid)" "Identifie le certificat de signataire de documents de la liste de confiance qui vérifie le DVC (J1 : 916ffa567c0f44a2)."
* #TD.J1.DE13 ^designation[0].language = #fr
* #TD.J1.DE13 ^designation[0].value = "Identifiant de clé (kid)"
* #TD.J2A.DE01 "Identifiant du ménage" "Le ménage de la liste de l'agent de santé communautaire auquel l'enfant est rattaché."
* #TD.J2A.DE01 ^designation[0].language = #fr
* #TD.J2A.DE01 ^designation[0].value = "Identifiant du ménage"
* #TD.J2A.DE02 "Prénom de l'enfant" "Le prénom de l'enfant."
* #TD.J2A.DE02 ^designation[0].language = #fr
* #TD.J2A.DE02 ^designation[0].value = "Prénom de l'enfant"
* #TD.J2A.DE03 "Nom de famille de l'enfant" "Le nom de famille de l'enfant."
* #TD.J2A.DE03 ^designation[0].language = #fr
* #TD.J2A.DE03 ^designation[0].value = "Nom de famille de l'enfant"
* #TD.J2A.DE04 "Date de naissance" "La date de naissance de l'enfant."
* #TD.J2A.DE04 ^designation[0].language = #fr
* #TD.J2A.DE04 ^designation[0].value = "Date de naissance"
* #TD.J2A.DE05 "Pays de naissance" "Le pays où l'enfant est né, s'il est né à l'étranger."
* #TD.J2A.DE05 ^designation[0].language = #fr
* #TD.J2A.DE05 ^designation[0].value = "Pays de naissance"
* #TD.J2A.DE06 "Cartes de vaccination étrangères détenues" "Indique si la famille détient des cartes de vaccination de l'étranger."
* #TD.J2A.DE06 ^designation[0].language = #fr
* #TD.J2A.DE06 ^designation[0].value = "Cartes de vaccination étrangères détenues"
* #TD.J2A.DE07 "Identifiant temporaire" "L'identifiant que porte l'enfant en attendant que l'enregistrement à l'état civil soit effectué."
* #TD.J2A.DE07 ^designation[0].language = #fr
* #TD.J2A.DE07 ^designation[0].value = "Identifiant temporaire"
* #TD.J2A.DE08 "Enregistré par" "L'agent de santé communautaire qui a enregistré l'enfant."
* #TD.J2A.DE08 ^designation[0].language = #fr
* #TD.J2A.DE08 ^designation[0].value = "Enregistré par"
* #TD.J2A.DE09 "Enregistré le" "Le moment où l'enregistrement a été saisi, sur le téléphone, éventuellement hors ligne."
* #TD.J2A.DE09 ^designation[0].language = #fr
* #TD.J2A.DE09 ^designation[0].value = "Enregistré le"
* #TD.J2A.DE10 "Informateur" "Le membre de la famille qui a donné les réponses."
* #TD.J2A.DE10 ^designation[0].language = #fr
* #TD.J2A.DE10 ^designation[0].value = "Informateur"
* #TD.J2A.DE11 "Dose lue sur une carte étrangère" "Une dose lue sur un DVC étranger par la lecture de tri sans vérification (STT-VER-011), enregistrée comme déclarée par la famille."
* #TD.J2A.DE11 ^designation[0].language = #fr
* #TD.J2A.DE11 ^designation[0].value = "Dose lue sur une carte étrangère"
* #TD.J2A.DE12 "Produit vaccinal (tel que lu)" "Le code produit de l'émetteur tel que lu sur la carte ; aucun code national n'est encore ajouté."
* #TD.J2A.DE12 ^designation[0].language = #fr
* #TD.J2A.DE12 ^designation[0].value = "Produit vaccinal (tel que lu)"
* #TD.J2A.DE13 "Date de vaccination (telle que lue)" "La date de vaccination telle que lue sur la carte."
* #TD.J2A.DE13 ^designation[0].language = #fr
* #TD.J2A.DE13 ^designation[0].value = "Date de vaccination (telle que lue)"
* #TD.J2A.DE14 "Numéro de lot (tel que lu)" "Le numéro de lot tel que lu sur la carte."
* #TD.J2A.DE14 ^designation[0].language = #fr
* #TD.J2A.DE14 ^designation[0].value = "Numéro de lot (tel que lu)"
* #TD.J2A.DE15 "Déclaré par" "Le membre de la famille qui a présenté la carte : la source d'information de la dose."
* #TD.J2A.DE15 ^designation[0].language = #fr
* #TD.J2A.DE15 ^designation[0].value = "Déclaré par"
* #TD.J2A.DE16 "Résultat consigné" "Toujours déclarée non vérifiée pour une lecture de tri (table de décision TD.DT.01) ; enregistrée avec primarySource false et une note."
* #TD.J2A.DE16 ^designation[0].language = #fr
* #TD.J2A.DE16 ^designation[0].value = "Résultat consigné"
* #TD.J2B.DE01 "Enfant" "L'enfant orienté."
* #TD.J2B.DE01 ^designation[0].language = #fr
* #TD.J2B.DE01 ^designation[0].value = "Enfant"
* #TD.J2B.DE02 "Orienté par" "L'agent de santé communautaire qui a fait l'orientation."
* #TD.J2B.DE02 ^designation[0].language = #fr
* #TD.J2B.DE02 ^designation[0].value = "Orienté par"
* #TD.J2B.DE03 "Orienté vers" "La clinique qui vérifiera les cartes."
* #TD.J2B.DE03 ^designation[0].language = #fr
* #TD.J2B.DE03 ^designation[0].value = "Orienté vers"
* #TD.J2B.DE04 "Orienté le" "Le moment où l'orientation a été faite."
* #TD.J2B.DE04 ^designation[0].language = #fr
* #TD.J2B.DE04 ^designation[0].value = "Orienté le"
* #TD.J2B.DE05 "Motif" "La raison de l'orientation de l'enfant : cartes de vaccination étrangères non vérifiées."
* #TD.J2B.DE05 ^designation[0].language = #fr
* #TD.J2B.DE05 ^designation[0].value = "Motif"
* #TD.J2B.DE06 "Doses à vérifier" "Les doses déclarées que la clinique est priée de vérifier."
* #TD.J2B.DE06 ^designation[0].language = #fr
* #TD.J2B.DE06 ^designation[0].value = "Doses à vérifier"
* #TD.J2B.DE07 "Statut de l'orientation" "Active jusqu'à ce que la clinique consigne un résultat pour chaque dose qu'elle énumère, puis terminée (indicateur TD.IND.03)."
* #TD.J2B.DE07 ^designation[0].language = #fr
* #TD.J2B.DE07 ^designation[0].value = "Statut de l'orientation"
* #TD.J3A.DE01 "Identifiant de clé (kid)" "Le kid du DVC vérifié, qui désigne le certificat du signataire."
* #TD.J3A.DE01 ^designation[0].language = #fr
* #TD.J3A.DE01 ^designation[0].value = "Identifiant de clé (kid)"
* #TD.J3A.DE02 "Pays émetteur" "Le participant qui a signé le DVC (CWT iss)."
* #TD.J3A.DE02 ^designation[0].language = #fr
* #TD.J3A.DE02 ^designation[0].value = "Pays émetteur"
* #TD.J3A.DE03 "Vérifié le" "Le moment où la vérification a été effectuée."
* #TD.J3A.DE03 ^designation[0].language = #fr
* #TD.J3A.DE03 ^designation[0].value = "Vérifié le"
* #TD.J3A.DE04 "Vérificateur" "Le système qui a vérifié le DVC."
* #TD.J3A.DE04 ^designation[0].language = #fr
* #TD.J3A.DE04 ^designation[0].value = "Vérificateur"
* #TD.J3A.DE05 "Résultat de la vérification" "Le résultat typé de la bibliothèque (STT-VER-008)."
* #TD.J3A.DE05 ^designation[0].language = #fr
* #TD.J3A.DE05 ^designation[0].value = "Résultat de la vérification"
* #TD.J3A.DE06 "Étape en échec" "L'étape à laquelle la vérification s'est arrêtée, en cas d'échec."
* #TD.J3A.DE06 ^designation[0].language = #fr
* #TD.J3A.DE06 ^designation[0].value = "Étape en échec"
* #TD.J3A.DE07 "Motif de l'échec" "La raison de l'arrêt de la vérification, en cas d'échec : l'entrée de la table de décision TD.DT.01."
* #TD.J3A.DE07 ^designation[0].language = #fr
* #TD.J3A.DE07 ^designation[0].value = "Motif de l'échec"
* #TD.J3A.DE08 "Liste de confiance actualisée le" "Le moment où le vérificateur a actualisé pour la dernière fois sa copie en cache de la liste de confiance ; un signataire ajouté depuis échoue avec KidNotFound (STT-VER-006)."
* #TD.J3A.DE08 ^designation[0].language = #fr
* #TD.J3A.DE08 ^designation[0].value = "Liste de confiance actualisée le"
* #TD.J3A.DE09 "Résultat consigné" "Ce que devient le DVC dans le dossier (table de décision TD.DT.01)."
* #TD.J3A.DE09 ^designation[0].language = #fr
* #TD.J3A.DE09 ^designation[0].value = "Résultat consigné"
* #TD.J3A.DE10 "Dose importée" "La dose enregistrée à partir du DVC vérifié."
* #TD.J3A.DE10 ^designation[0].language = #fr
* #TD.J3A.DE10 ^designation[0].value = "Dose importée"
* #TD.J3A.DE11 "Dose déclarée remplacée" "La dose déclarée que la dose vérifiée remplace."
* #TD.J3A.DE11 ^designation[0].language = #fr
* #TD.J3A.DE11 ^designation[0].value = "Dose déclarée remplacée"
* #TD.J3A.DE12 "Politique de confiance" "Le cadre de confiance au titre duquel le DVC a été vérifié."
* #TD.J3A.DE12 ^designation[0].language = #fr
* #TD.J3A.DE12 ^designation[0].value = "Politique de confiance"
* #TD.J3B.DE01 "Code produit de l'émetteur" "Le code du vaccin tel que l'émetteur l'a signé ; conservé, jamais remplacé (STD-SEM-001)."
* #TD.J3B.DE01 ^designation[0].language = #fr
* #TD.J3B.DE01 ^designation[0].value = "Code produit de l'émetteur"
* #TD.J3B.DE02 "Code du calendrier national" "Le code antigène et dose du calendrier national, ajouté à côté du code produit. Absent pour une dose sans correspondance, que le profil TrustDemoOnesaImmunization (onesaEpi 1..1) ne représente pas encore."
* #TD.J3B.DE02 ^designation[0].language = #fr
* #TD.J3B.DE02 ^designation[0].value = "Code du calendrier national"
* #TD.J3B.DE03 "Base de la correspondance" "Comment le code du calendrier a été trouvé (table de décision TD.DT.02)."
* #TD.J3B.DE03 ^designation[0].language = #fr
* #TD.J3B.DE03 ^designation[0].value = "Base de la correspondance"
* #TD.J3B.DE04 "Confirmé par" "Le clinicien qui a confirmé un équivalent que la table de correspondance ne couvrait pas."
* #TD.J3B.DE04 ^designation[0].language = #fr
* #TD.J3B.DE04 ^designation[0].value = "Confirmé par"
* #TD.J3B.DE05 "Compte pour le calendrier" "Indique si le calendrier compte la dose (table de décision TD.DT.03) : seules les doses provenant d'une source primaire et dotées d'un code du calendrier national."
* #TD.J3B.DE05 ^designation[0].language = #fr
* #TD.J3B.DE05 ^designation[0].value = "Compte pour le calendrier"
* #TD.J3B.DE06 "Dose due" "Une dose du calendrier national que l'évaluation juge due (table de décision TD.DT.04)."
* #TD.J3B.DE06 ^designation[0].language = #fr
* #TD.J3B.DE06 ^designation[0].value = "Dose due"
* #TD.J3B.DE07 "Dose du calendrier" "Le code antigène et dose du calendrier pour la dose due."
* #TD.J3B.DE07 ^designation[0].language = #fr
* #TD.J3B.DE07 ^designation[0].value = "Dose du calendrier"
* #TD.J3B.DE08 "Statut de la prévision" "La prévision pour la dose."
* #TD.J3B.DE08 ^designation[0].language = #fr
* #TD.J3B.DE08 ^designation[0].value = "Statut de la prévision"
* #TD.J3B.DE09 "Date d'échéance" "La date de naissance de l'enfant plus l'âge de référence de l'action du calendrier."
* #TD.J3B.DE09 ^designation[0].language = #fr
* #TD.J3B.DE09 ^designation[0].value = "Date d'échéance"
* #TD.J3B.DE10 "Rappel" "Le rappel créé pour la prochaine visite."
* #TD.J3B.DE10 ^designation[0].language = #fr
* #TD.J3B.DE10 ^designation[0].value = "Rappel"
* #TD.J40.DE01 "Sujet" "Le membre de la famille dont le résumé est partagé."
* #TD.J40.DE01 ^designation[0].language = #fr
* #TD.J40.DE01 ^designation[0].value = "Sujet"
* #TD.J40.DE02 "Titulaire" "La personne qui partage le lien et décide qui peut l'ouvrir."
* #TD.J40.DE02 ^designation[0].language = #fr
* #TD.J40.DE02 ^designation[0].value = "Titulaire"
* #TD.J40.DE03 "Dépositaire" "Le service du pays d'origine qui héberge le dossier et vérifie chaque demande."
* #TD.J40.DE03 ^designation[0].language = #fr
* #TD.J40.DE03 ^designation[0].value = "Dépositaire"
* #TD.J40.DE04 "Document partagé" "Le résumé du patient que le lien communique."
* #TD.J40.DE04 ^designation[0].language = #fr
* #TD.J40.DE04 ^designation[0].value = "Document partagé"
* #TD.J40.DE05 "Valide à partir du" "Le premier jour où le lien peut être ouvert."
* #TD.J40.DE05 ^designation[0].language = #fr
* #TD.J40.DE05 ^designation[0].value = "Valide à partir du"
* #TD.J40.DE06 "Valide jusqu'au" "L'expiration choisie par le titulaire ; après celle-ci, le lien ne communique plus rien (STD-ACC-001)."
* #TD.J40.DE06 ^designation[0].language = #fr
* #TD.J40.DE06 ^designation[0].value = "Valide jusqu'au"
* #TD.J40.DE07 "Finalité" "La finalité d'utilisation que le titulaire autorise (J4 : traitement)."
* #TD.J40.DE07 ^designation[0].language = #fr
* #TD.J40.DE07 ^designation[0].value = "Finalité"
* #TD.J40.DE08 "Code d'accès défini" "Indique si le titulaire a protégé le lien par un code d'accès. Le code d'accès lui-même n'est jamais conservé dans le dossier."
* #TD.J40.DE08 ^designation[0].language = #fr
* #TD.J40.DE08 ^designation[0].value = "Code d'accès défini"
* #TD.J40.DE09 "Retiré le" "Le moment où le titulaire a retiré le lien, le cas échéant."
* #TD.J40.DE09 ^designation[0].language = #fr
* #TD.J40.DE09 ^designation[0].value = "Retiré le"
* #TD.J41.DE01 "Demandé le" "Le moment où la demande est arrivée."
* #TD.J41.DE01 ^designation[0].language = #fr
* #TD.J41.DE01 ^designation[0].value = "Demandé le"
* #TD.J41.DE02 "Demandeur" "Le système destinataire à l'étranger qui a demandé le manifeste."
* #TD.J41.DE02 ^designation[0].language = #fr
* #TD.J41.DE02 ^designation[0].value = "Demandeur"
* #TD.J41.DE03 "Adresse réseau du demandeur" "La provenance de la demande."
* #TD.J41.DE03 ^designation[0].language = #fr
* #TD.J41.DE03 ^designation[0].value = "Adresse réseau du demandeur"
* #TD.J41.DE04 "Dépositaire" "La passerelle du pays d'origine qui a répondu à la demande et l'a journalisée."
* #TD.J41.DE04 ^designation[0].language = #fr
* #TD.J41.DE04 ^designation[0].value = "Dépositaire"
* #TD.J41.DE05 "Patient" "Le patient dont le dossier a été demandé."
* #TD.J41.DE05 ^designation[0].language = #fr
* #TD.J41.DE05 ^designation[0].value = "Patient"
* #TD.J41.DE06 "Communiqué" "Indique si le manifeste a été communiqué (table de décision TD.DT.05)."
* #TD.J41.DE06 ^designation[0].language = #fr
* #TD.J41.DE06 ^designation[0].value = "Communiqué"
* #TD.J41.DE07 "Résultat de l'audit" "0 en cas de communication ; 4 (échec mineur) en cas de refus."
* #TD.J41.DE07 ^designation[0].language = #fr
* #TD.J41.DE07 ^designation[0].value = "Résultat de l'audit"
* #TD.J41.DE08 "Motif du refus" "La raison pour laquelle rien n'a été communiqué, en cas de refus."
* #TD.J41.DE08 ^designation[0].language = #fr
* #TD.J41.DE08 ^designation[0].value = "Motif du refus"
* #TD.J41.DE09 "Consentement" "Le consentement du titulaire au regard duquel la demande a été vérifiée."
* #TD.J41.DE09 ^designation[0].language = #fr
* #TD.J41.DE09 ^designation[0].value = "Consentement"
* #TD.J41.DE10 "Document communiqué" "Le résumé communiqué, en cas de communication."
* #TD.J41.DE10 ^designation[0].language = #fr
* #TD.J41.DE10 ^designation[0].value = "Document communiqué"

CodeSystem: TrustDemoVerificationResultFr
Id: TrustDemoVerificationResult-fr
Title: "Résultat de la lecture d'un DVC"
Description: "French (fr) supplement to TrustDemoVerificationResult: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationResult)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 3
* #verified "Vérifié" "Toutes les étapes de la vérification ont réussi (STT-VER-001)."
* #verified ^designation[0].language = #fr
* #verified ^designation[0].value = "Vérifié"
* #failed "Échec" "La vérification s'est arrêtée à une étape, pour un motif tiré de l'ensemble fermé de STT-VER-008."
* #failed ^designation[0].language = #fr
* #failed ^designation[0].value = "Échec"
* #unverified "Lu, non vérifié" "La charge utile a été lue par read-unverified, sans consultation de la liste de confiance ni contrôle de la signature (STT-VER-011)."
* #unverified ^designation[0].language = #fr
* #unverified ^designation[0].value = "Lu, non vérifié"

CodeSystem: TrustDemoVerificationStepFr
Id: TrustDemoVerificationStep-fr
Title: "Étapes de la vérification"
Description: "French (fr) supplement to TrustDemoVerificationStep: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationStep)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 12
* #prefix "Préfixe" "Le préfixe de contexte HC1: et sa version."
* #prefix ^designation[0].language = #fr
* #prefix ^designation[0].value = "Préfixe"
* #base45 "Base45" "Décodage Base45 du texte du code QR."
* #base45 ^designation[0].language = #fr
* #base45 ^designation[0].value = "Base45"
* #inflate "Décompression" "Décompression ZLIB, dans les limites fixées."
* #inflate ^designation[0].language = #fr
* #inflate ^designation[0].value = "Décompression"
* #cose "COSE" "Analyse de la structure COSE_Sign1."
* #cose ^designation[0].language = #fr
* #cose ^designation[0].value = "COSE"
* #header "En-tête" "Les en-têtes protégés et non protégés."
* #header ^designation[0].language = #fr
* #header ^designation[0].value = "En-tête"
* #trust-lookup "Consultation de la liste de confiance" "Recherche du certificat du signataire par son kid dans la liste de confiance."
* #trust-lookup ^designation[0].language = #fr
* #trust-lookup ^designation[0].value = "Consultation de la liste de confiance"
* #signature "Signature" "Contrôle de la signature avec la clé du signataire."
* #signature ^designation[0].language = #fr
* #signature ^designation[0].value = "Signature"
* #key-usage "Usage de la clé" "Contrôle que le certificat du signataire peut signer ce type de certificat."
* #key-usage ^designation[0].language = #fr
* #key-usage ^designation[0].value = "Usage de la clé"
* #cwt "CWT" "Lecture de l'ensemble de revendications CWT."
* #cwt ^designation[0].language = #fr
* #cwt ^designation[0].value = "CWT"
* #time "Date et heure" "Contrôle de la date d'émission et de l'expiration au regard de l'horloge du vérificateur."
* #time ^designation[0].language = #fr
* #time ^designation[0].value = "Date et heure"
* #hcert "HCERT" "Recherche de la revendication hcert et de sa sous-revendication."
* #hcert ^designation[0].language = #fr
* #hcert ^designation[0].value = "HCERT"
* #payload "Charge utile" "Lecture de la charge utile au regard de son modèle logique."
* #payload ^designation[0].language = #fr
* #payload ^designation[0].value = "Charge utile"

CodeSystem: TrustDemoVerificationFailureReasonFr
Id: TrustDemoVerificationFailureReason-fr
Title: "Motifs d'échec de la vérification"
Description: "French (fr) supplement to TrustDemoVerificationFailureReason: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationFailureReason)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 16
* #BadPrefix "Préfixe incorrect" "Le texte ne commence pas par le préfixe HC1:."
* #BadPrefix ^designation[0].language = #fr
* #BadPrefix ^designation[0].value = "Préfixe incorrect"
* #UnsupportedContextVersion "Version de contexte non prise en charge" "L'identifiant de contexte désigne une version que le vérificateur ne prend pas en charge."
* #UnsupportedContextVersion ^designation[0].language = #fr
* #UnsupportedContextVersion ^designation[0].value = "Version de contexte non prise en charge"
* #Base45Invalid "Base45 non valide" "Le texte n'est pas du Base45 valide."
* #Base45Invalid ^designation[0].language = #fr
* #Base45Invalid ^designation[0].value = "Base45 non valide"
* #InflateFailed "Échec de la décompression" "Les octets compressés ne se décompressent pas."
* #InflateFailed ^designation[0].language = #fr
* #InflateFailed ^designation[0].value = "Échec de la décompression"
* #LimitExceeded "Limite dépassée" "Une limite de décodage (taille ou profondeur) a été dépassée."
* #LimitExceeded ^designation[0].language = #fr
* #LimitExceeded ^designation[0].value = "Limite dépassée"
* #CoseMalformed "COSE mal formé" "Les octets ne forment pas une structure COSE_Sign1 bien formée."
* #CoseMalformed ^designation[0].language = #fr
* #CoseMalformed ^designation[0].value = "COSE mal formé"
* #HeaderInvalid "En-tête non valide" "Un en-tête COSE est absent ou non conforme aux exigences."
* #HeaderInvalid ^designation[0].language = #fr
* #HeaderInvalid ^designation[0].value = "En-tête non valide"
* #UnsupportedAlgorithm "Algorithme non pris en charge" "L'algorithme de signature ne fait pas partie de ceux qu'accepte le vérificateur."
* #UnsupportedAlgorithm ^designation[0].language = #fr
* #UnsupportedAlgorithm ^designation[0].value = "Algorithme non pris en charge"
* #KidNotFound "Clé introuvable" "Aucun certificat de la copie de la liste de confiance du vérificateur ne porte ce kid (STT-VER-006)."
* #KidNotFound ^designation[0].language = #fr
* #KidNotFound ^designation[0].value = "Clé introuvable"
* #SignatureInvalid "Signature non valide" "La signature ne se vérifie avec aucun certificat portant ce kid."
* #SignatureInvalid ^designation[0].language = #fr
* #SignatureInvalid ^designation[0].value = "Signature non valide"
* #KeyUsageMismatch "Usage de la clé non conforme" "Le certificat du signataire ne peut pas signer ce type de certificat."
* #KeyUsageMismatch ^designation[0].language = #fr
* #KeyUsageMismatch ^designation[0].value = "Usage de la clé non conforme"
* #Expired "Expiré" "La date d'expiration du certificat est dépassée."
* #Expired ^designation[0].language = #fr
* #Expired ^designation[0].value = "Expiré"
* #NotYetValid "Pas encore valide" "La date d'émission du certificat se situe dans le futur."
* #NotYetValid ^designation[0].language = #fr
* #NotYetValid ^designation[0].value = "Pas encore valide"
* #HcertMissing "HCERT absent" "L'ensemble de revendications ne comporte pas de revendication hcert."
* #HcertMissing ^designation[0].language = #fr
* #HcertMissing ^designation[0].value = "HCERT absent"
* #MultipleSubclaims "Sous-revendications multiples" "La revendication hcert comporte plus de sous-revendications que le vérificateur n'en accepte."
* #MultipleSubclaims ^designation[0].language = #fr
* #MultipleSubclaims ^designation[0].value = "Sous-revendications multiples"
* #PayloadInvalid "Charge utile non valide" "La charge utile n'est pas conforme à son modèle logique."
* #PayloadInvalid ^designation[0].language = #fr
* #PayloadInvalid ^designation[0].value = "Charge utile non valide"

CodeSystem: TrustDemoDvcOutcomeFr
Id: TrustDemoDvcOutcome-fr
Title: "Ce que devient un DVC scanné dans le dossier"
Description: "French (fr) supplement to TrustDemoDvcOutcome: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoDvcOutcome)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 4
* #verified "Vérifié" "Enregistré à partir de sa source primaire, avec la provenance de la vérification."
* #verified ^designation[0].language = #fr
* #verified ^designation[0].value = "Vérifié"
* #reported-unverified "Déclaré, non vérifié" "Conservé comme déclaré par la famille (primarySource false) ; non pris en compte par le calendrier."
* #reported-unverified ^designation[0].language = #fr
* #reported-unverified ^designation[0].value = "Déclaré, non vérifié"
* #rejected "Rejeté" "Le certificat ne constitue pas une preuve de dose ; l'étape et le motif sont enregistrés."
* #rejected ^designation[0].language = #fr
* #rejected ^designation[0].value = "Rejeté"
* #not-read "Non lu" "Rien n'a pu être lu dans le code QR ; la carte est traitée comme une carte papier."
* #not-read ^designation[0].language = #fr
* #not-read ^designation[0].value = "Non lu"

CodeSystem: TrustDemoCodeMappingBasisFr
Id: TrustDemoCodeMappingBasis-fr
Title: "Comment une dose importée a obtenu son code du calendrier national"
Description: "French (fr) supplement to TrustDemoCodeMappingBasis: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoCodeMappingBasis)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 4
* #concept-map "Par la ConceptMap nationale" "Le code produit de l'émetteur a un code du calendrier équivalent dans la table de correspondance nationale."
* #concept-map ^designation[0].language = #fr
* #concept-map ^designation[0].value = "Par la ConceptMap nationale"
* #clinician-confirmed "Confirmé par le clinicien" "La table de correspondance n'avait pas d'entrée ; le clinicien a confirmé l'équivalent, et la décision est ajoutée à la table de correspondance."
* #clinician-confirmed ^designation[0].language = #fr
* #clinician-confirmed ^designation[0].value = "Confirmé par le clinicien"
* #unmapped "Sans correspondance" "Aucun équivalent n'est connu ; le code de l'émetteur est conservé tel quel et affiché comme sans correspondance."
* #unmapped ^designation[0].language = #fr
* #unmapped ^designation[0].value = "Sans correspondance"
* #not-imported "Non importée" "La dose n'a pas été vérifiée ; elle n'a donc été ni importée ni mise en correspondance."
* #not-imported ^designation[0].language = #fr
* #not-imported ^designation[0].value = "Non importée"

CodeSystem: TrustDemoVhlRefusalReasonFr
Id: TrustDemoVhlRefusalReason-fr
Title: "Pourquoi un lien partagé n'a rien communiqué"
Description: "French (fr) supplement to TrustDemoVhlRefusalReason: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVhlRefusalReason)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 3
* #withdrawn "Retiré" "Le titulaire a retiré le lien avant son expiration."
* #withdrawn ^designation[0].language = #fr
* #withdrawn ^designation[0].value = "Retiré"
* #expired "Expiré" "La demande est arrivée après l'expiration choisie par le titulaire."
* #expired ^designation[0].language = #fr
* #expired ^designation[0].value = "Expiré"
* #wrong-passcode "Code d'accès erroné" "Le code d'accès fourni ne correspond pas à celui défini par le titulaire."
* #wrong-passcode ^designation[0].language = #fr
* #wrong-passcode ^designation[0].value = "Code d'accès erroné"

CodeSystem: TrustDemoTrustDomainFr
Id: TrustDemoTrustDomain-fr
Title: "Domaines de confiance des parcours (illustratifs)"
Description: "French (fr) supplement to TrustDemoTrustDomain: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoTrustDomain)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 2
* #DEMO-DVC "Démo : certificat de vaccination numérique" "DVC de vaccination de routine (HCERT) signés dose par dose par le système d'un centre de naissance et vérifiés par le DSE d'un centre de santé du pays de résidence (J1, J3)."
* #DEMO-DVC ^designation[0].language = #fr
* #DEMO-DVC ^designation[0].value = "Démo : certificat de vaccination numérique"
* #DEMO-VHL "Démo : lien de santé vérifiable" "Liens de santé vérifiables (HCERT) vers un résumé du patient, créés sur le portail national et résolus à un point de soins à l'étranger (J4.0, J4.1). Ses conditions d'utilisation sont TrustDemoVhlTermsOfUse."
* #DEMO-VHL ^designation[0].language = #fr
* #DEMO-VHL ^designation[0].value = "Démo : lien de santé vérifiable"

CodeSystem: TrustDemoVhlConsentFr
Id: TrustDemoVhlConsent-fr
Title: "Consentements du domaine de confiance VHL de la démo (illustratifs)"
Description: "French (fr) supplement to TrustDemoVhlConsent: displays and definitions in French. Unofficial agent translation."
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVhlConsent)
* ^language = #fr
* ^status = #draft
* ^experimental = true
* ^count = 1
* #CONSENT-VHL-TREATMENT "Consentement à la lecture du résumé à des fins de traitement" "Toute personne à qui le titulaire remet le code QR et le code d'accès du VHL peut lire le résumé du patient auquel il donne accès, à des fins de traitement, jusqu'à l'expiration du lien. Chaque accès est journalisé par le portail émetteur."
* #CONSENT-VHL-TREATMENT ^designation[0].language = #fr
* #CONSENT-VHL-TREATMENT ^designation[0].value = "Consentement à la lecture du résumé à des fins de traitement"
