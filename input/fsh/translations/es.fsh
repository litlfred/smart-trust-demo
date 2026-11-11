// Spanish (es) CodeSystem supplements for this IG's own CodeSystems.
// Agent translation, UNOFFICIAL and unreviewed: no human sign-off. One file per locale;
// the CodeSystems themselves are not edited. Displays and definitions mirror translations/es/.

CodeSystem: TrustDemoVaccineProductEs
Id: TrustDemoVaccineProduct-es
Title: "Productos vacunales (códigos ilustrativos al estilo PreQual)"
Description: "Suplemento en español (es) de TrustDemoVaccineProduct: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVaccineProduct)
* ^language = #es
* ^caseSensitive = true
* #vp-hepb-peds-monovalent "Vacuna contra la hepatitis B, pediátrica, monovalente"
  * ^designation[0].language = #es
  * ^designation[0].value = "Vacuna contra la hepatitis B, pediátrica, monovalente"
* #vp-bcg-freeze-dried "Vacuna BCG, liofilizada"
  * ^designation[0].language = #es
  * ^designation[0].value = "Vacuna BCG, liofilizada"
* #vp-pentavalent-liquid "DTP-HepB-Hib (pentavalente), líquida"
  * ^designation[0].language = #es
  * ^designation[0].value = "DTP-HepB-Hib (pentavalente), líquida"
* #vp-bopv-drops "Vacuna antipoliomielítica oral bivalente (bOPV), gotas"
  * ^designation[0].language = #es
  * ^designation[0].value = "Vacuna antipoliomielítica oral bivalente (bOPV), gotas"
* #vp-pcv-13-dose "Vacuna antineumocócica conjugada (PCV)"
  * ^designation[0].language = #es
  * ^designation[0].value = "Vacuna antineumocócica conjugada (PCV)"
* #vp-mr-freeze-dried "Vacuna contra el sarampión y la rubéola, liofilizada"
  * ^designation[0].language = #es
  * ^designation[0].value = "Vacuna contra el sarampión y la rubéola, liofilizada"

CodeSystem: TrustDemoOnesaEpiScheduleEs
Id: TrustDemoOnesaEpiSchedule-es
Title: "Códigos de antígeno y dosis del calendario nacional (ilustrativos, Onesa)"
Description: "Suplemento en español (es) de TrustDemoOnesaEpiSchedule: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoOnesaEpiSchedule)
* ^language = #es
* ^caseSensitive = true
* #XXK-EPI-HEPB-BD "Hepatitis B, dosis al nacer"
  * ^designation[0].language = #es
  * ^designation[0].value = "Hepatitis B, dosis al nacer"
* #XXK-EPI-BCG "BCG"
  * ^designation[0].language = #es
  * ^designation[0].value = "BCG"
* #XXK-EPI-PENTA-1 "Pentavalente (DTP-HepB-Hib), dosis 1"
  * ^designation[0].language = #es
  * ^designation[0].value = "Pentavalente (DTP-HepB-Hib), dosis 1"
* #XXK-EPI-OPV-1 "bOPV, dosis 1"
  * ^designation[0].language = #es
  * ^designation[0].value = "bOPV, dosis 1"
* #XXK-EPI-PCV-1 "PCV, dosis 1"
  * ^designation[0].language = #es
  * ^designation[0].value = "PCV, dosis 1"
* #XXK-EPI-MR-1 "Sarampión y rubéola, dosis 1"
  * ^designation[0].language = #es
  * ^designation[0].value = "Sarampión y rubéola, dosis 1"

CodeSystem: TrustDemoDataElementsEs
Id: TrustDemoDataElements-es
Title: "Elementos de datos de los recorridos"
Description: "Suplemento en español (es) de TrustDemoDataElements: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoDataElements)
* ^language = #es
* ^caseSensitive = true
* #TD.J1.DE01 "Nombre" "El nombre del niño/a tal como lo registra el hospital de nacimiento."
  * ^designation[0].language = #es
  * ^designation[0].value = "Nombre"
* #TD.J1.DE02 "Fecha de nacimiento" "La fecha de nacimiento del niño/a."
  * ^designation[0].language = #es
  * ^designation[0].value = "Fecha de nacimiento"
* #TD.J1.DE03 "Nombre del progenitor o tutor" "El progenitor o tutor, para un sujeto sin documento de identidad, como un recién nacido (STT-PAY-005)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Nombre del progenitor o tutor"
* #TD.J1.DE04 "Número de historia hospitalaria" "El identificador propio que el hospital de nacimiento asigna al niño/a. No se incluye en el DVC."
  * ^designation[0].language = #es
  * ^designation[0].value = "Número de historia hospitalaria"
* #TD.J1.DE05 "Producto vacunal" "El producto administrado, en la codificación de productos del emisor (códigos ilustrativos al estilo PreQual)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Producto vacunal"
* #TD.J1.DE06 "Fecha de vacunación" "La fecha en que se administró la dosis. El registro hospitalario guarda también la hora; el DVC lleva la fecha."
  * ^designation[0].language = #es
  * ^designation[0].value = "Fecha de vacunación"
* #TD.J1.DE07 "Número de lote" "El lote de la vacuna administrada."
  * ^designation[0].language = #es
  * ^designation[0].value = "Número de lote"
* #TD.J1.DE08 "Número de dosis" "El número de la dosis en su serie. Lo registra el hospital; la carga útil mínima del DVC no lo incluye."
  * ^designation[0].language = #es
  * ^designation[0].value = "Número de dosis"
* #TD.J1.DE09 "Clínico supervisor" "El clínico que administró o supervisó la dosis."
  * ^designation[0].language = #es
  * ^designation[0].value = "Clínico supervisor"
* #TD.J1.DE10 "País emisor" "El participante de la red de confianza cuya clave firma el DVC (J1: XXR)."
  * ^designation[0].language = #es
  * ^designation[0].value = "País emisor"
* #TD.J1.DE11 "Emitido el" "Cuándo se firmó el DVC."
  * ^designation[0].language = #es
  * ^designation[0].value = "Emitido el"
* #TD.J1.DE12 "Caduca el" "Cuándo deja de verificarse el DVC, si el emisor fija una caducidad."
  * ^designation[0].language = #es
  * ^designation[0].value = "Caduca el"
* #TD.J1.DE13 "Identificador de clave (kid)" "Identifica el certificado del firmante de documentos de la lista de confianza que verifica el DVC (J1: 916ffa567c0f44a2)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Identificador de clave (kid)"
* #TD.J2A.DE01 "Identificador del hogar" "El hogar del padrón del CHW al que se incorpora el niño/a."
  * ^designation[0].language = #es
  * ^designation[0].value = "Identificador del hogar"
* #TD.J2A.DE02 "Nombre del niño/a" "El nombre del niño/a."
  * ^designation[0].language = #es
  * ^designation[0].value = "Nombre del niño/a"
* #TD.J2A.DE03 "Apellido del niño/a" "El apellido del niño/a."
  * ^designation[0].language = #es
  * ^designation[0].value = "Apellido del niño/a"
* #TD.J2A.DE04 "Fecha de nacimiento" "La fecha de nacimiento del niño/a."
  * ^designation[0].language = #es
  * ^designation[0].value = "Fecha de nacimiento"
* #TD.J2A.DE05 "País de nacimiento" "El país en que nació el niño/a, cuando nació en el extranjero."
  * ^designation[0].language = #es
  * ^designation[0].value = "País de nacimiento"
* #TD.J2A.DE06 "Tarjetas de vacunación extranjeras en posesión" "Si la familia tiene tarjetas de vacunación del extranjero."
  * ^designation[0].language = #es
  * ^designation[0].value = "Tarjetas de vacunación extranjeras en posesión"
* #TD.J2A.DE07 "Identificador temporal" "El identificador que lleva el niño/a hasta que el registro civil se pone al día."
  * ^designation[0].language = #es
  * ^designation[0].value = "Identificador temporal"
* #TD.J2A.DE08 "Registrado por" "El agente comunitario de salud que registró al niño/a."
  * ^designation[0].language = #es
  * ^designation[0].value = "Registrado por"
* #TD.J2A.DE09 "Registrado el" "Cuándo se capturó el registro, en el teléfono, posiblemente sin conexión."
  * ^designation[0].language = #es
  * ^designation[0].value = "Registrado el"
* #TD.J2A.DE10 "Informante" "El miembro de la familia que dio las respuestas."
  * ^designation[0].language = #es
  * ^designation[0].value = "Informante"
* #TD.J2A.DE11 "Dosis leída de una tarjeta extranjera" "Una dosis leída de un DVC extranjero con la lectura de triaje no verificada (STT-VER-011), guardada tal como la notificó la familia."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dosis leída de una tarjeta extranjera"
* #TD.J2A.DE12 "Producto vacunal (según la lectura)" "El código de producto del emisor tal como se leyó de la tarjeta; todavía no se añade ningún código nacional."
  * ^designation[0].language = #es
  * ^designation[0].value = "Producto vacunal (según la lectura)"
* #TD.J2A.DE13 "Fecha de vacunación (según la lectura)" "La fecha de vacunación tal como se leyó de la tarjeta."
  * ^designation[0].language = #es
  * ^designation[0].value = "Fecha de vacunación (según la lectura)"
* #TD.J2A.DE14 "Número de lote (según la lectura)" "El número de lote tal como se leyó de la tarjeta."
  * ^designation[0].language = #es
  * ^designation[0].value = "Número de lote (según la lectura)"
* #TD.J2A.DE15 "Notificado por" "El miembro de la familia que mostró la tarjeta: la fuente de información de la dosis."
  * ^designation[0].language = #es
  * ^designation[0].value = "Notificado por"
* #TD.J2A.DE16 "Resultado en el registro" "Siempre notificada sin verificar en una lectura de triaje (tabla de decisión TD.DT.01); se registra como primarySource false con una nota."
  * ^designation[0].language = #es
  * ^designation[0].value = "Resultado en el registro"
* #TD.J2B.DE01 "Niño/a" "El niño/a derivado."
  * ^designation[0].language = #es
  * ^designation[0].value = "Niño/a"
* #TD.J2B.DE02 "Derivado por" "El agente comunitario de salud que hizo la derivación."
  * ^designation[0].language = #es
  * ^designation[0].value = "Derivado por"
* #TD.J2B.DE03 "Derivado a" "La clínica que verificará las tarjetas."
  * ^designation[0].language = #es
  * ^designation[0].value = "Derivado a"
* #TD.J2B.DE04 "Derivado el" "Cuándo se hizo la derivación."
  * ^designation[0].language = #es
  * ^designation[0].value = "Derivado el"
* #TD.J2B.DE05 "Motivo" "Por qué se deriva al niño/a: tarjetas de vacunación extranjeras sin verificar."
  * ^designation[0].language = #es
  * ^designation[0].value = "Motivo"
* #TD.J2B.DE06 "Dosis por verificar" "Las dosis notificadas que se pide a la clínica verificar."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dosis por verificar"
* #TD.J2B.DE07 "Estado de la derivación" "Activa hasta que la clínica registra un resultado para cada dosis que enumera; después, completada (indicador TD.IND.03)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Estado de la derivación"
* #TD.J3A.DE01 "Identificador de clave (kid)" "El kid del DVC verificado, que identifica el certificado del firmante."
  * ^designation[0].language = #es
  * ^designation[0].value = "Identificador de clave (kid)"
* #TD.J3A.DE02 "País emisor" "El participante que firmó el DVC (CWT iss)."
  * ^designation[0].language = #es
  * ^designation[0].value = "País emisor"
* #TD.J3A.DE03 "Verificado el" "Cuándo se realizó la verificación."
  * ^designation[0].language = #es
  * ^designation[0].value = "Verificado el"
* #TD.J3A.DE04 "Verificador" "El sistema que verificó el DVC."
  * ^designation[0].language = #es
  * ^designation[0].value = "Verificador"
* #TD.J3A.DE05 "Resultado de la verificación" "El resultado tipado de la biblioteca (STT-VER-008)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Resultado de la verificación"
* #TD.J3A.DE06 "Paso fallido" "El paso en el que se detuvo la verificación, cuando falló."
  * ^designation[0].language = #es
  * ^designation[0].value = "Paso fallido"
* #TD.J3A.DE07 "Motivo del fallo" "Por qué se detuvo la verificación, cuando falló: la entrada de la tabla de decisión TD.DT.01."
  * ^designation[0].language = #es
  * ^designation[0].value = "Motivo del fallo"
* #TD.J3A.DE08 "Lista de confianza actualizada el" "Cuándo actualizó el verificador por última vez su copia en caché de la lista de confianza; un firmante añadido después falla con KidNotFound (STT-VER-006)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Lista de confianza actualizada el"
* #TD.J3A.DE09 "Resultado en el registro" "En qué se convierte el DVC en el registro (tabla de decisión TD.DT.01)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Resultado en el registro"
* #TD.J3A.DE10 "Dosis importada" "La dosis registrada a partir del DVC verificado."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dosis importada"
* #TD.J3A.DE11 "Dosis notificada sustituida" "La dosis notificada que sustituye la verificada."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dosis notificada sustituida"
* #TD.J3A.DE12 "Política de confianza" "El marco de confianza conforme al cual se verificó el DVC."
  * ^designation[0].language = #es
  * ^designation[0].value = "Política de confianza"
* #TD.J3B.DE01 "Código de producto del emisor" "El código de la vacuna tal como lo firmó el emisor; se conserva y nunca se sustituye (STD-SEM-001)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Código de producto del emisor"
* #TD.J3B.DE02 "Código del calendario nacional" "El código de antígeno y dosis del calendario nacional, añadido junto al código de producto. Ausente en una dosis sin correspondencia, que el perfil TrustDemoOnesaImmunization (onesaEpi 1..1) todavía no representa."
  * ^designation[0].language = #es
  * ^designation[0].value = "Código del calendario nacional"
* #TD.J3B.DE03 "Base de la correspondencia" "Cómo se encontró el código del calendario (tabla de decisión TD.DT.02)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Base de la correspondencia"
* #TD.J3B.DE04 "Confirmado por" "El clínico que confirmó un equivalente que la correspondencia no cubría."
  * ^designation[0].language = #es
  * ^designation[0].value = "Confirmado por"
* #TD.J3B.DE05 "Cuenta para el calendario" "Si el calendario cuenta la dosis (tabla de decisión TD.DT.03): solo las dosis de una fuente primaria con un código del calendario nacional."
  * ^designation[0].language = #es
  * ^designation[0].value = "Cuenta para el calendario"
* #TD.J3B.DE06 "Dosis pendiente" "Una dosis del calendario nacional que la evaluación determina como pendiente (tabla de decisión TD.DT.04)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dosis pendiente"
* #TD.J3B.DE07 "Dosis del calendario" "El código de antígeno y dosis del calendario para la dosis pendiente."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dosis del calendario"
* #TD.J3B.DE08 "Estado de la previsión" "La previsión para la dosis."
  * ^designation[0].language = #es
  * ^designation[0].value = "Estado de la previsión"
* #TD.J3B.DE09 "Fecha prevista" "La fecha de nacimiento del niño/a más la edad de aplicación de la acción del calendario."
  * ^designation[0].language = #es
  * ^designation[0].value = "Fecha prevista"
* #TD.J3B.DE10 "Recordatorio" "El recordatorio creado para la próxima visita."
  * ^designation[0].language = #es
  * ^designation[0].value = "Recordatorio"
* #TD.J40.DE01 "Sujeto" "El miembro de la familia cuyo resumen se comparte."
  * ^designation[0].language = #es
  * ^designation[0].value = "Sujeto"
* #TD.J40.DE02 "Titular" "La persona que comparte el enlace y decide quién puede abrirlo."
  * ^designation[0].language = #es
  * ^designation[0].value = "Titular"
* #TD.J40.DE03 "Custodio" "El servicio del país de origen que aloja el registro y comprueba cada solicitud."
  * ^designation[0].language = #es
  * ^designation[0].value = "Custodio"
* #TD.J40.DE04 "Documento compartido" "El resumen del paciente que entrega el enlace."
  * ^designation[0].language = #es
  * ^designation[0].value = "Documento compartido"
* #TD.J40.DE05 "Válido desde" "El primer día en que se puede abrir el enlace."
  * ^designation[0].language = #es
  * ^designation[0].value = "Válido desde"
* #TD.J40.DE06 "Válido hasta" "La fecha de caducidad que eligió el titular; después de ella, el enlace no entrega nada (STD-ACC-001)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Válido hasta"
* #TD.J40.DE07 "Finalidad" "La finalidad de uso que permite el titular (J4: tratamiento)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Finalidad"
* #TD.J40.DE08 "Código de acceso establecido" "Si el titular protegió el enlace con un código de acceso. El código de acceso en sí nunca se almacena en el registro."
  * ^designation[0].language = #es
  * ^designation[0].value = "Código de acceso establecido"
* #TD.J40.DE09 "Retirado el" "Cuándo retiró el enlace el titular, si lo hizo."
  * ^designation[0].language = #es
  * ^designation[0].value = "Retirado el"
* #TD.J41.DE01 "Solicitado el" "Cuándo llegó la solicitud."
  * ^designation[0].language = #es
  * ^designation[0].value = "Solicitado el"
* #TD.J41.DE02 "Solicitante" "El sistema receptor en el extranjero que solicitó el manifiesto."
  * ^designation[0].language = #es
  * ^designation[0].value = "Solicitante"
* #TD.J41.DE03 "Dirección de red del solicitante" "De dónde procedía la solicitud."
  * ^designation[0].language = #es
  * ^designation[0].value = "Dirección de red del solicitante"
* #TD.J41.DE04 "Custodio" "La pasarela del país de origen que respondió a la solicitud y la registró."
  * ^designation[0].language = #es
  * ^designation[0].value = "Custodio"
* #TD.J41.DE05 "Patient" "De quién es el registro solicitado."
  * ^designation[0].language = #es
  * ^designation[0].value = "Patient"
* #TD.J41.DE06 "Entregado" "Si se entregó el manifiesto (tabla de decisión TD.DT.05)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Entregado"
* #TD.J41.DE07 "Resultado de auditoría" "0 cuando se entrega; 4 (fallo menor) cuando se rechaza."
  * ^designation[0].language = #es
  * ^designation[0].value = "Resultado de auditoría"
* #TD.J41.DE08 "Motivo del rechazo" "Por qué no se entregó nada, cuando se rechazó."
  * ^designation[0].language = #es
  * ^designation[0].value = "Motivo del rechazo"
* #TD.J41.DE09 "Consentimiento" "El consentimiento del titular con el que se contrastó la solicitud."
  * ^designation[0].language = #es
  * ^designation[0].value = "Consentimiento"
* #TD.J41.DE10 "Documento entregado" "El resumen entregado, cuando se entrega."
  * ^designation[0].language = #es
  * ^designation[0].value = "Documento entregado"

CodeSystem: TrustDemoVerificationResultEs
Id: TrustDemoVerificationResult-es
Title: "Resultado de la lectura de un DVC"
Description: "Suplemento en español (es) de TrustDemoVerificationResult: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationResult)
* ^language = #es
* ^caseSensitive = true
* #verified "Verificado" "Se superaron todos los pasos de la verificación (STT-VER-001)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Verificado"
* #failed "Fallido" "La verificación se detuvo en un paso, por un motivo del conjunto cerrado de STT-VER-008."
  * ^designation[0].language = #es
  * ^designation[0].value = "Fallido"
* #unverified "Leído, no verificado" "La carga útil se leyó con read-unverified, sin consulta de confianza ni comprobación de firma (STT-VER-011)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Leído, no verificado"

CodeSystem: TrustDemoVerificationStepEs
Id: TrustDemoVerificationStep-es
Title: "Pasos de verificación"
Description: "Suplemento en español (es) de TrustDemoVerificationStep: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationStep)
* ^language = #es
* ^caseSensitive = true
* #prefix "Prefijo" "El prefijo de contexto HC1: y su versión."
  * ^designation[0].language = #es
  * ^designation[0].value = "Prefijo"
* #base45 "Base45" "Decodificación Base45 del texto del QR."
  * ^designation[0].language = #es
  * ^designation[0].value = "Base45"
* #inflate "Descompresión" "Descompresión ZLIB, dentro de los límites."
  * ^designation[0].language = #es
  * ^designation[0].value = "Descompresión"
* #cose "COSE" "Análisis de la estructura COSE_Sign1."
  * ^designation[0].language = #es
  * ^designation[0].value = "COSE"
* #header "Encabezado" "Los encabezados protegidos y no protegidos."
  * ^designation[0].language = #es
  * ^designation[0].value = "Encabezado"
* #trust-lookup "Consulta de confianza" "Búsqueda del certificado del firmante por kid en la lista de confianza."
  * ^designation[0].language = #es
  * ^designation[0].value = "Consulta de confianza"
* #signature "Firma" "Comprobación de la firma con la clave del firmante."
  * ^designation[0].language = #es
  * ^designation[0].value = "Firma"
* #key-usage "Uso de la clave" "Comprobación de que el certificado del firmante puede firmar este tipo de certificado."
  * ^designation[0].language = #es
  * ^designation[0].value = "Uso de la clave"
* #cwt "CWT" "Lectura del conjunto de declaraciones (claims) CWT."
  * ^designation[0].language = #es
  * ^designation[0].value = "CWT"
* #time "Hora" "Comprobación de la emisión y la caducidad con el reloj del verificador."
  * ^designation[0].language = #es
  * ^designation[0].value = "Hora"
* #hcert "HCERT" "Búsqueda de la declaración hcert y de su subdeclaración."
  * ^designation[0].language = #es
  * ^designation[0].value = "HCERT"
* #payload "Carga útil" "Lectura de la carga útil según su modelo lógico."
  * ^designation[0].language = #es
  * ^designation[0].value = "Carga útil"

CodeSystem: TrustDemoVerificationFailureReasonEs
Id: TrustDemoVerificationFailureReason-es
Title: "Motivos de fallo de la verificación"
Description: "Suplemento en español (es) de TrustDemoVerificationFailureReason: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationFailureReason)
* ^language = #es
* ^caseSensitive = true
* #BadPrefix "Prefijo incorrecto" "El texto no empieza con el prefijo HC1:."
  * ^designation[0].language = #es
  * ^designation[0].value = "Prefijo incorrecto"
* #UnsupportedContextVersion "Versión de contexto no admitida" "El identificador de contexto indica una versión que el verificador no admite."
  * ^designation[0].language = #es
  * ^designation[0].value = "Versión de contexto no admitida"
* #Base45Invalid "Base45 no válido" "El texto no es Base45 válido."
  * ^designation[0].language = #es
  * ^designation[0].value = "Base45 no válido"
* #InflateFailed "Descompresión fallida" "Los bytes comprimidos no se descomprimen."
  * ^designation[0].language = #es
  * ^designation[0].value = "Descompresión fallida"
* #LimitExceeded "Límite superado" "Se superó un límite de decodificación (tamaño o profundidad)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Límite superado"
* #CoseMalformed "COSE mal formado" "Los bytes no son un COSE_Sign1 bien formado."
  * ^designation[0].language = #es
  * ^designation[0].value = "COSE mal formado"
* #HeaderInvalid "Encabezado no válido" "Falta un encabezado COSE o no es como se requiere."
  * ^designation[0].language = #es
  * ^designation[0].value = "Encabezado no válido"
* #UnsupportedAlgorithm "Algoritmo no admitido" "El algoritmo de firma no es uno que el verificador acepte."
  * ^designation[0].language = #es
  * ^designation[0].value = "Algoritmo no admitido"
* #KidNotFound "Clave no encontrada" "Ningún certificado de la copia de la lista de confianza del verificador tiene el kid (STT-VER-006)."
  * ^designation[0].language = #es
  * ^designation[0].value = "Clave no encontrada"
* #SignatureInvalid "Firma no válida" "La firma no se verifica con ningún certificado que tenga el kid."
  * ^designation[0].language = #es
  * ^designation[0].value = "Firma no válida"
* #KeyUsageMismatch "Uso de la clave no coincidente" "El certificado del firmante no puede firmar este tipo de certificado."
  * ^designation[0].language = #es
  * ^designation[0].value = "Uso de la clave no coincidente"
* #Expired "Caducado" "La fecha de caducidad del certificado ya pasó."
  * ^designation[0].language = #es
  * ^designation[0].value = "Caducado"
* #NotYetValid "Aún no válido" "La hora de emisión del certificado está en el futuro."
  * ^designation[0].language = #es
  * ^designation[0].value = "Aún no válido"
* #HcertMissing "Falta HCERT" "El conjunto de declaraciones no tiene declaración hcert."
  * ^designation[0].language = #es
  * ^designation[0].value = "Falta HCERT"
* #MultipleSubclaims "Varias subdeclaraciones" "La declaración hcert tiene más subdeclaraciones de las que el verificador acepta."
  * ^designation[0].language = #es
  * ^designation[0].value = "Varias subdeclaraciones"
* #PayloadInvalid "Carga útil no válida" "La carga útil no se ajusta a su modelo lógico."
  * ^designation[0].language = #es
  * ^designation[0].value = "Carga útil no válida"

CodeSystem: TrustDemoDvcOutcomeEs
Id: TrustDemoDvcOutcome-es
Title: "En qué se convierte en el registro un DVC escaneado"
Description: "Suplemento en español (es) de TrustDemoDvcOutcome: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoDvcOutcome)
* ^language = #es
* ^caseSensitive = true
* #verified "Verificado" "Registrado a partir de su fuente primaria, con la procedencia de la verificación."
  * ^designation[0].language = #es
  * ^designation[0].value = "Verificado"
* #reported-unverified "Notificado, no verificado" "Se conserva tal como lo notificó la familia (primarySource false); el calendario no lo cuenta."
  * ^designation[0].language = #es
  * ^designation[0].value = "Notificado, no verificado"
* #rejected "Rechazado" "El certificado no es prueba de una dosis; se registran el paso y el motivo."
  * ^designation[0].language = #es
  * ^designation[0].value = "Rechazado"
* #not-read "No leído" "No se pudo leer nada del QR; la tarjeta se trata como papel."
  * ^designation[0].language = #es
  * ^designation[0].value = "No leído"

CodeSystem: TrustDemoCodeMappingBasisEs
Id: TrustDemoCodeMappingBasis-es
Title: "Cómo obtuvo una dosis importada su código del calendario nacional"
Description: "Suplemento en español (es) de TrustDemoCodeMappingBasis: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoCodeMappingBasis)
* ^language = #es
* ^caseSensitive = true
* #concept-map "Por el ConceptMap nacional" "El código de producto del emisor tiene un código equivalente del calendario en la tabla nacional de correspondencias."
  * ^designation[0].language = #es
  * ^designation[0].value = "Por el ConceptMap nacional"
* #clinician-confirmed "Confirmado por el profesional clínico" "La tabla no tenía ninguna entrada; el profesional clínico confirmó la equivalencia, y la decisión se añade a la tabla."
  * ^designation[0].language = #es
  * ^designation[0].value = "Confirmado por el profesional clínico"
* #unmapped "Sin correspondencia" "No se conoce ninguna equivalencia; el código del emisor se conserva tal cual y se muestra sin correspondencia."
  * ^designation[0].language = #es
  * ^designation[0].value = "Sin correspondencia"
* #not-imported "No importado" "La dosis no se verificó, así que no se importó ni se le asignó correspondencia."
  * ^designation[0].language = #es
  * ^designation[0].value = "No importado"

CodeSystem: TrustDemoVhlRefusalReasonEs
Id: TrustDemoVhlRefusalReason-es
Title: "Por qué un enlace compartido no entregó nada"
Description: "Suplemento en español (es) de TrustDemoVhlRefusalReason: designaciones de cada concepto. Traducción no oficial generada por un agente, sin revisión humana."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVhlRefusalReason)
* ^language = #es
* ^caseSensitive = true
* #withdrawn "Retirado" "El titular retiró el enlace antes de que caducara."
  * ^designation[0].language = #es
  * ^designation[0].value = "Retirado"
* #expired "Caducado" "La solicitud llegó después de la fecha de caducidad que eligió el titular."
  * ^designation[0].language = #es
  * ^designation[0].value = "Caducado"
* #wrong-passcode "Código de acceso incorrecto" "El código de acceso indicado no coincide con el que fijó el titular."
  * ^designation[0].language = #es
  * ^designation[0].value = "Código de acceso incorrecto"
