// Arabic (ar) CodeSystem supplements for this IG's own CodeSystems.
// Agent translation, UNOFFICIAL and unreviewed: no human sign-off. One file per locale;
// the CodeSystems themselves are not edited. Displays and definitions mirror translations/ar/.

CodeSystem: TrustDemoVaccineProductAr
Id: TrustDemoVaccineProduct-ar
Title: "منتجات اللقاحات (رموز توضيحية على نمط PreQual)"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoVaccineProduct: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVaccineProduct)
* ^language = #ar
* ^caseSensitive = true
* #vp-hepb-peds-monovalent "لقاح التهاب الكبد B، للأطفال، أحادي التكافؤ"
  * ^designation[0].language = #ar
  * ^designation[0].value = "لقاح التهاب الكبد B، للأطفال، أحادي التكافؤ"
* #vp-bcg-freeze-dried "لقاح BCG، مُجفَّد"
  * ^designation[0].language = #ar
  * ^designation[0].value = "لقاح BCG، مُجفَّد"
* #vp-pentavalent-liquid "DTP-HepB-Hib (خماسي التكافؤ)، سائل"
  * ^designation[0].language = #ar
  * ^designation[0].value = "DTP-HepB-Hib (خماسي التكافؤ)، سائل"
* #vp-bopv-drops "لقاح شلل الأطفال الفموي ثنائي التكافؤ (bOPV)، قطرات"
  * ^designation[0].language = #ar
  * ^designation[0].value = "لقاح شلل الأطفال الفموي ثنائي التكافؤ (bOPV)، قطرات"
* #vp-pcv-13-dose "لقاح المكورات الرئوية المقترن (PCV)"
  * ^designation[0].language = #ar
  * ^designation[0].value = "لقاح المكورات الرئوية المقترن (PCV)"
* #vp-mr-freeze-dried "لقاح الحصبة والحصبة الألمانية، مُجفَّد"
  * ^designation[0].language = #ar
  * ^designation[0].value = "لقاح الحصبة والحصبة الألمانية، مُجفَّد"

CodeSystem: TrustDemoLaoEpiScheduleAr
Id: TrustDemoLaoEpiSchedule-ar
Title: "رموز المستضدات والجرعات في جدول التطعيم الوطني (توضيحية، جمهورية لاو الديمقراطية الشعبية (Lao PDR))"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoLaoEpiSchedule: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoLaoEpiSchedule)
* ^language = #ar
* ^caseSensitive = true
* #LAO-EPI-HEPB-BD "جرعة الولادة من لقاح التهاب الكبد B"
  * ^designation[0].language = #ar
  * ^designation[0].value = "جرعة الولادة من لقاح التهاب الكبد B"
* #LAO-EPI-BCG "BCG"
  * ^designation[0].language = #ar
  * ^designation[0].value = "BCG"
* #LAO-EPI-PENTA-1 "خماسي التكافؤ (DTP-HepB-Hib)، الجرعة 1"
  * ^designation[0].language = #ar
  * ^designation[0].value = "خماسي التكافؤ (DTP-HepB-Hib)، الجرعة 1"
* #LAO-EPI-OPV-1 "bOPV، الجرعة 1"
  * ^designation[0].language = #ar
  * ^designation[0].value = "bOPV، الجرعة 1"
* #LAO-EPI-PCV-1 "PCV، الجرعة 1"
  * ^designation[0].language = #ar
  * ^designation[0].value = "PCV، الجرعة 1"
* #LAO-EPI-MR-1 "الحصبة والحصبة الألمانية، الجرعة 1"
  * ^designation[0].language = #ar
  * ^designation[0].value = "الحصبة والحصبة الألمانية، الجرعة 1"

CodeSystem: TrustDemoDataElementsAr
Id: TrustDemoDataElements-ar
Title: "عناصر بيانات الرحلات"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoDataElements: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoDataElements)
* ^language = #ar
* ^caseSensitive = true
* #TD.J1.DE01 "الاسم" "اسم الطفل كما يسجله مستشفى الولادة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الاسم"
* #TD.J1.DE02 "تاريخ الولادة" "تاريخ ولادة الطفل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تاريخ الولادة"
* #TD.J1.DE03 "اسم الوالد أو الوصي" "الوالد أو الوصي، لشخص معنيّ ليست لديه وثيقة هوية، مثل المولود الجديد (STT-PAY-005)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "اسم الوالد أو الوصي"
* #TD.J1.DE04 "رقم المستشفى" "المعرِّف الخاص بمستشفى الولادة للطفل. لا تحمله شهادة DVC."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رقم المستشفى"
* #TD.J1.DE05 "منتج اللقاح" "المنتج المُعطى، بترميز المنتجات لدى الجهة المُصدِرة (رموز توضيحية على نمط PreQual)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "منتج اللقاح"
* #TD.J1.DE06 "تاريخ التطعيم" "تاريخ إعطاء الجرعة. يحتفظ سجل المستشفى بالوقت أيضًا؛ وتحمل شهادة DVC التاريخ."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تاريخ التطعيم"
* #TD.J1.DE07 "رقم التشغيلة" "تشغيلة (دفعة) اللقاح المُعطى."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رقم التشغيلة"
* #TD.J1.DE08 "رقم الجرعة" "رقم الجرعة في سلسلتها. يسجله المستشفى؛ ولا تحمله الحمولة الدنيا لشهادة DVC."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رقم الجرعة"
* #TD.J1.DE09 "الممارس السريري المشرف" "الممارس السريري الذي أعطى الجرعة أو أشرف على إعطائها."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الممارس السريري المشرف"
* #TD.J1.DE10 "البلد المُصدِر" "المشارك في شبكة الثقة الذي يوقّع مفتاحه شهادة DVC (J1: XXR)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "البلد المُصدِر"
* #TD.J1.DE11 "صدرت في" "متى وُقِّعت شهادة DVC."
  * ^designation[0].language = #ar
  * ^designation[0].value = "صدرت في"
* #TD.J1.DE12 "تنتهي صلاحيتها في" "متى تتوقف شهادة DVC عن اجتياز التحقق، حيث تحدد الجهة المُصدِرة تاريخ انتهاء صلاحية."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تنتهي صلاحيتها في"
* #TD.J1.DE13 "معرِّف المفتاح (kid)" "يحدد شهادة موقِّع المستندات (DSC) في قائمة الثقة التي تتحقق من DVC (J1: 916ffa567c0f44a2)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "معرِّف المفتاح (kid)"
* #TD.J2A.DE01 "معرِّف الأسرة المعيشية" "الأسرة المعيشية المدرجة في قائمة عامل الصحة المجتمعي (CHW) التي ينضم إليها الطفل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "معرِّف الأسرة المعيشية"
* #TD.J2A.DE02 "الاسم الأول للطفل" "الاسم الأول للطفل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الاسم الأول للطفل"
* #TD.J2A.DE03 "اسم عائلة الطفل" "اسم عائلة الطفل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "اسم عائلة الطفل"
* #TD.J2A.DE04 "تاريخ الولادة" "تاريخ ولادة الطفل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تاريخ الولادة"
* #TD.J2A.DE05 "بلد الولادة" "البلد الذي وُلد فيه الطفل، إذا كان في الخارج."
  * ^designation[0].language = #ar
  * ^designation[0].value = "بلد الولادة"
* #TD.J2A.DE06 "بطاقات التطعيم الأجنبية المحفوظة" "ما إذا كانت الأسرة تحمل بطاقات تطعيم من الخارج."
  * ^designation[0].language = #ar
  * ^designation[0].value = "بطاقات التطعيم الأجنبية المحفوظة"
* #TD.J2A.DE07 "المعرِّف المؤقت" "المعرِّف الذي يحمله الطفل إلى أن يستكمل التسجيل المدني."
  * ^designation[0].language = #ar
  * ^designation[0].value = "المعرِّف المؤقت"
* #TD.J2A.DE08 "سجّله" "عامل الصحة المجتمعي الذي سجّل الطفل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "سجّله"
* #TD.J2A.DE09 "سُجِّل في" "متى التُقط التسجيل، على الهاتف، وربما دون اتصال."
  * ^designation[0].language = #ar
  * ^designation[0].value = "سُجِّل في"
* #TD.J2A.DE10 "المُخبِر" "فرد الأسرة الذي قدّم الإجابات."
  * ^designation[0].language = #ar
  * ^designation[0].value = "المُخبِر"
* #TD.J2A.DE11 "جرعة مقروءة من بطاقة أجنبية" "جرعة واحدة قُرئت من DVC أجنبية بالقراءة الأولية غير المُتحقَّق منها (STT-VER-011)، وحُفظت كما أبلغت عنها الأسرة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "جرعة مقروءة من بطاقة أجنبية"
* #TD.J2A.DE12 "منتج اللقاح (كما قُرئ)" "رمز المنتج لدى الجهة المُصدِرة كما قُرئ من البطاقة؛ ولم يُضَف رمز وطني بعد."
  * ^designation[0].language = #ar
  * ^designation[0].value = "منتج اللقاح (كما قُرئ)"
* #TD.J2A.DE13 "تاريخ التطعيم (كما قُرئ)" "تاريخ التطعيم كما قُرئ من البطاقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تاريخ التطعيم (كما قُرئ)"
* #TD.J2A.DE14 "رقم التشغيلة (كما قُرئ)" "رقم التشغيلة كما قُرئ من البطاقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رقم التشغيلة (كما قُرئ)"
* #TD.J2A.DE15 "أبلغ عنه" "فرد الأسرة الذي أبرز البطاقة: مصدر معلومات الجرعة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أبلغ عنه"
* #TD.J2A.DE16 "نتيجة السجل" "دائمًا «مُبلَّغ عنها غير متحقَّق منها» في قراءة الفرز الأولي (جدول القرار TD.DT.01)؛ وتُسجَّل بقيمة primarySource false مع ملاحظة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "نتيجة السجل"
* #TD.J2B.DE01 "الطفل" "الطفل المُحال."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الطفل"
* #TD.J2B.DE02 "أحاله" "عامل الصحة المجتمعي الذي أجرى الإحالة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أحاله"
* #TD.J2B.DE03 "أُحيل إلى" "العيادة التي ستتحقق من البطاقات."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أُحيل إلى"
* #TD.J2B.DE04 "أُحيل في" "متى أُجريت الإحالة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أُحيل في"
* #TD.J2B.DE05 "السبب" "سبب إحالة الطفل: بطاقات تطعيم أجنبية غير متحقَّق منها."
  * ^designation[0].language = #ar
  * ^designation[0].value = "السبب"
* #TD.J2B.DE06 "الجرعات المطلوب التحقق منها" "الجرعات المُبلَّغ عنها التي يُطلب من العيادة التحقق منها."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجرعات المطلوب التحقق منها"
* #TD.J2B.DE07 "حالة الإحالة" "نشطة إلى أن تسجل العيادة نتيجة لكل جرعة تدرجها، ثم مكتملة (المؤشر TD.IND.03)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "حالة الإحالة"
* #TD.J3A.DE01 "معرِّف المفتاح (kid)" "قيمة kid لشهادة DVC المتحقَّق منها، والتي تسمّي شهادة الموقِّع."
  * ^designation[0].language = #ar
  * ^designation[0].value = "معرِّف المفتاح (kid)"
* #TD.J3A.DE02 "البلد المُصدِر" "المشارك الذي وقّع شهادة DVC (CWT iss)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "البلد المُصدِر"
* #TD.J3A.DE03 "تم التحقق في" "متى جرى التحقق."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تم التحقق في"
* #TD.J3A.DE04 "الجهة المُتحقِّقة" "النظام الذي تحقق من شهادة DVC."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجهة المُتحقِّقة"
* #TD.J3A.DE05 "نتيجة التحقق" "النتيجة المُصنَّفة الأنواع للمكتبة (STT-VER-008)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "نتيجة التحقق"
* #TD.J3A.DE06 "الخطوة التي أخفقت" "الخطوة التي توقف عندها التحقق، عند إخفاقه."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الخطوة التي أخفقت"
* #TD.J3A.DE07 "سبب الإخفاق" "لماذا توقف التحقق، عند إخفاقه: مُدخَل جدول القرار TD.DT.01."
  * ^designation[0].language = #ar
  * ^designation[0].value = "سبب الإخفاق"
* #TD.J3A.DE08 "حُدِّثت قائمة الثقة في" "آخر مرة حدّثت فيها الجهة المُتحقِّقة نسختها المخزَّنة مؤقتًا من قائمة الثقة؛ يفشل أي موقِّع أُضيف بعد ذلك بالخطأ KidNotFound (STT-VER-006)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "حُدِّثت قائمة الثقة في"
* #TD.J3A.DE09 "نتيجة السجل" "ما تصبح عليه شهادة DVC في السجل (جدول القرار TD.DT.01)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "نتيجة السجل"
* #TD.J3A.DE10 "الجرعة المستوردة" "الجرعة المسجلة من شهادة DVC المتحقَّق منها."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجرعة المستوردة"
* #TD.J3A.DE11 "الجرعة المُبلَّغ عنها المُستبدَلة" "الجرعة المُبلَّغ عنها التي تحلّ محلها الجرعة المتحقَّق منها."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجرعة المُبلَّغ عنها المُستبدَلة"
* #TD.J3A.DE12 "سياسة الثقة" "إطار الثقة الذي جرى التحقق من شهادة DVC بموجبه."
  * ^designation[0].language = #ar
  * ^designation[0].value = "سياسة الثقة"
* #TD.J3B.DE01 "رمز المنتج لدى الجهة المُصدِرة" "رمز اللقاح كما وقّعته الجهة المُصدِرة؛ يُحفَظ ولا يُستبدَل أبدًا (STD-SEM-001)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رمز المنتج لدى الجهة المُصدِرة"
* #TD.J3B.DE02 "رمز جدول التطعيم الوطني" "رمز المستضد والجرعة في جدول التطعيم الوطني، يُضاف بجانب رمز المنتج. ويغيب في حالة الجرعة غير المربوطة، التي لا يمثّلها ملف التعريف TrustDemoLaoImmunization (laoEpi 1..1) بعد."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رمز جدول التطعيم الوطني"
* #TD.J3B.DE03 "أساس الربط" "كيف وُجد رمز جدول التطعيم (جدول القرار TD.DT.02)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أساس الربط"
* #TD.J3B.DE04 "أكّده" "الممارس السريري الذي أكّد مكافئًا لم تغطِّه الخريطة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أكّده"
* #TD.J3B.DE05 "تُحتسب ضمن جدول التطعيم" "ما إذا كان جدول التطعيم يحتسب الجرعة (جدول القرار TD.DT.03): فقط الجرعات الصادرة عن مصدر أولي والتي لها رمز في جدول التطعيم الوطني."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تُحتسب ضمن جدول التطعيم"
* #TD.J3B.DE06 "الجرعة المستحقة" "جرعة من جدول التطعيم الوطني يجد التقييم أنها مستحقة (جدول القرار TD.DT.04)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجرعة المستحقة"
* #TD.J3B.DE07 "جرعة جدول التطعيم" "رمز المستضد والجرعة في جدول التطعيم للجرعة المستحقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "جرعة جدول التطعيم"
* #TD.J3B.DE08 "حالة التوقع" "التوقع الخاص بالجرعة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "حالة التوقع"
* #TD.J3B.DE09 "تاريخ الاستحقاق" "تاريخ ولادة الطفل مضافًا إليه العمر المحدد لتوقيت إجراء جدول التطعيم."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تاريخ الاستحقاق"
* #TD.J3B.DE10 "التذكير" "التذكير المُنشأ للزيارة التالية."
  * ^designation[0].language = #ar
  * ^designation[0].value = "التذكير"
* #TD.J40.DE01 "الموضوع" "فرد الأسرة الذي يُشارَك ملخّصه."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الموضوع"
* #TD.J40.DE02 "الحامل" "الشخص الذي يُشارك الرابط ويقرر من يجوز له فتحه."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الحامل"
* #TD.J40.DE03 "الجهة الحافظة" "خدمة البلد الأم التي تستضيف السجل وتفحص كل طلب."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجهة الحافظة"
* #TD.J40.DE04 "المستند المُشارَك" "ملخّص المريض الذي يُتيحه الرابط."
  * ^designation[0].language = #ar
  * ^designation[0].value = "المستند المُشارَك"
* #TD.J40.DE05 "صالح من" "أول يوم يجوز فيه فتح الرابط."
  * ^designation[0].language = #ar
  * ^designation[0].value = "صالح من"
* #TD.J40.DE06 "صالح حتى" "تاريخ انتهاء الصلاحية الذي اختاره الحامل؛ بعده لا يُتيح الرابط أي شيء (STD-ACC-001)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "صالح حتى"
* #TD.J40.DE07 "الغرض" "غرض الاستخدام الذي يسمح به الحامل (J4: العلاج)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الغرض"
* #TD.J40.DE08 "تم تعيين رمز المرور" "ما إذا كان الحامل قد حمى الرابط برمز مرور. لا يُخزَّن رمز المرور نفسه في السجل أبدًا."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تم تعيين رمز المرور"
* #TD.J40.DE09 "سُحب في" "متى سحب الحامل الرابط، إن فعل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "سُحب في"
* #TD.J41.DE01 "طُلب في" "متى وصل الطلب."
  * ^designation[0].language = #ar
  * ^designation[0].value = "طُلب في"
* #TD.J41.DE02 "مقدِّم الطلب" "النظام المُستقبِل في الخارج الذي طلب البيان."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مقدِّم الطلب"
* #TD.J41.DE03 "عنوان الشبكة لمقدِّم الطلب" "من أين جاء الطلب."
  * ^designation[0].language = #ar
  * ^designation[0].value = "عنوان الشبكة لمقدِّم الطلب"
* #TD.J41.DE04 "الجهة الحافظة" "بوابة الربط في البلد الأم التي ردّت على الطلب وسجّلته."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الجهة الحافظة"
* #TD.J41.DE05 "Patient" "سجلّ من طُلب."
  * ^designation[0].language = #ar
  * ^designation[0].value = "Patient"
* #TD.J41.DE06 "أُتيح" "ما إذا أُتيح البيان (جدول القرار TD.DT.05)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "أُتيح"
* #TD.J41.DE07 "نتيجة التدقيق" "0 عند الإتاحة؛ 4 (إخفاق بسيط) عند الرفض."
  * ^designation[0].language = #ar
  * ^designation[0].value = "نتيجة التدقيق"
* #TD.J41.DE08 "سبب الرفض" "لماذا لم يُتَح أي شيء، عند الرفض."
  * ^designation[0].language = #ar
  * ^designation[0].value = "سبب الرفض"
* #TD.J41.DE09 "Consent" "موافقة الحامل التي فُحص الطلب في ضوئها."
  * ^designation[0].language = #ar
  * ^designation[0].value = "Consent"
* #TD.J41.DE10 "المستند المُتاح" "الملخّص المُتاح، عند الإتاحة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "المستند المُتاح"

CodeSystem: TrustDemoVerificationResultAr
Id: TrustDemoVerificationResult-ar
Title: "نتيجة قراءة DVC"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoVerificationResult: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationResult)
* ^language = #ar
* ^caseSensitive = true
* #verified "مُتحقَّق منها" "اجتازت جميع خطوات التحقق بنجاح (STT-VER-001)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مُتحقَّق منها"
* #failed "فشل" "توقف التحقق عند خطوة ما، لسبب من المجموعة المغلقة في STT-VER-008."
  * ^designation[0].language = #ar
  * ^designation[0].value = "فشل"
* #unverified "مقروءة، غير مُتحقَّق منها" "قُرئت الحمولة بواسطة read-unverified، دون بحث في قائمة الثقة أو تحقق من التوقيع (STT-VER-011)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مقروءة، غير مُتحقَّق منها"

CodeSystem: TrustDemoVerificationStepAr
Id: TrustDemoVerificationStep-ar
Title: "خطوات التحقق"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoVerificationStep: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationStep)
* ^language = #ar
* ^caseSensitive = true
* #prefix "البادئة" "بادئة السياق HC1: والإصدار."
  * ^designation[0].language = #ar
  * ^designation[0].value = "البادئة"
* #base45 "Base45" "فك ترميز Base45 لنص رمز QR."
  * ^designation[0].language = #ar
  * ^designation[0].value = "Base45"
* #inflate "فك الضغط" "فك ضغط ZLIB، ضمن الحدود."
  * ^designation[0].language = #ar
  * ^designation[0].value = "فك الضغط"
* #cose "COSE" "تحليل بنية COSE_Sign1."
  * ^designation[0].language = #ar
  * ^designation[0].value = "COSE"
* #header "الترويسة" "الترويستان المحمية وغير المحمية."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الترويسة"
* #trust-lookup "البحث في قائمة الثقة" "العثور على شهادة الموقِّع بواسطة kid في قائمة الثقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "البحث في قائمة الثقة"
* #signature "التوقيع" "التحقق من التوقيع باستخدام مفتاح الموقِّع."
  * ^designation[0].language = #ar
  * ^designation[0].value = "التوقيع"
* #key-usage "استخدام المفتاح" "التحقق من أن شهادة الموقِّع مخوَّلة بتوقيع هذا النوع من الشهادات."
  * ^designation[0].language = #ar
  * ^designation[0].value = "استخدام المفتاح"
* #cwt "CWT" "قراءة مجموعة مطالبات CWT."
  * ^designation[0].language = #ar
  * ^designation[0].value = "CWT"
* #time "الوقت" "التحقق من وقت الإصدار وتاريخ انتهاء الصلاحية مقابل ساعة الجهة المُتحقِّقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الوقت"
* #hcert "HCERT" "العثور على مطالبة hcert ومطالبتها الفرعية."
  * ^designation[0].language = #ar
  * ^designation[0].value = "HCERT"
* #payload "الحمولة" "قراءة الحمولة مقابل نموذجها المنطقي."
  * ^designation[0].language = #ar
  * ^designation[0].value = "الحمولة"

CodeSystem: TrustDemoVerificationFailureReasonAr
Id: TrustDemoVerificationFailureReason-ar
Title: "أسباب فشل التحقق"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoVerificationFailureReason: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVerificationFailureReason)
* ^language = #ar
* ^caseSensitive = true
* #BadPrefix "بادئة غير صالحة" "لا يبدأ النص بالبادئة HC1:."
  * ^designation[0].language = #ar
  * ^designation[0].value = "بادئة غير صالحة"
* #UnsupportedContextVersion "إصدار سياق غير مدعوم" "يشير معرِّف السياق إلى إصدار لا تدعمه الجهة المُتحقِّقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "إصدار سياق غير مدعوم"
* #Base45Invalid "Base45 غير صالح" "النص ليس Base45 صالحًا."
  * ^designation[0].language = #ar
  * ^designation[0].value = "Base45 غير صالح"
* #InflateFailed "فشل فك الضغط" "تعذّر فك ضغط البايتات المضغوطة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "فشل فك الضغط"
* #LimitExceeded "تم تجاوز الحد" "تم تجاوز أحد حدود فك الترميز (الحجم أو العمق)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "تم تجاوز الحد"
* #CoseMalformed "COSE مشوَّه" "البايتات ليست بنية COSE_Sign1 سليمة التكوين."
  * ^designation[0].language = #ar
  * ^designation[0].value = "COSE مشوَّه"
* #HeaderInvalid "ترويسة غير صالحة" "ترويسة COSE مفقودة أو غير مطابقة للمطلوب."
  * ^designation[0].language = #ar
  * ^designation[0].value = "ترويسة غير صالحة"
* #UnsupportedAlgorithm "خوارزمية غير مدعومة" "خوارزمية التوقيع ليست من الخوارزميات التي تقبلها الجهة المُتحقِّقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "خوارزمية غير مدعومة"
* #KidNotFound "المفتاح غير موجود" "لا توجد في نسخة الجهة المُتحقِّقة من قائمة الثقة أي شهادة تحمل هذا الـ kid (STT-VER-006)."
  * ^designation[0].language = #ar
  * ^designation[0].value = "المفتاح غير موجود"
* #SignatureInvalid "توقيع غير صالح" "لا يمكن التحقق من التوقيع باستخدام أي شهادة تحمل هذا الـ kid."
  * ^designation[0].language = #ar
  * ^designation[0].value = "توقيع غير صالح"
* #KeyUsageMismatch "عدم تطابق استخدام المفتاح" "شهادة الموقِّع غير مخوَّلة بتوقيع هذا النوع من الشهادات."
  * ^designation[0].language = #ar
  * ^designation[0].value = "عدم تطابق استخدام المفتاح"
* #Expired "منتهية الصلاحية" "انقضى تاريخ انتهاء صلاحية الشهادة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "منتهية الصلاحية"
* #NotYetValid "لم تصبح صالحة بعد" "وقت إصدار الشهادة يقع في المستقبل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "لم تصبح صالحة بعد"
* #HcertMissing "HCERT مفقودة" "لا تحتوي مجموعة المطالبات على مطالبة hcert."
  * ^designation[0].language = #ar
  * ^designation[0].value = "HCERT مفقودة"
* #MultipleSubclaims "مطالبات فرعية متعددة" "تحتوي مطالبة hcert على مطالبات فرعية أكثر مما تقبله الجهة المُتحقِّقة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مطالبات فرعية متعددة"
* #PayloadInvalid "حمولة غير صالحة" "الحمولة لا تتوافق مع نموذجها المنطقي."
  * ^designation[0].language = #ar
  * ^designation[0].value = "حمولة غير صالحة"

CodeSystem: TrustDemoDvcOutcomeAr
Id: TrustDemoDvcOutcome-ar
Title: "ما تصبح عليه DVC الممسوحة ضوئيًا في السجل"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoDvcOutcome: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoDvcOutcome)
* ^language = #ar
* ^caseSensitive = true
* #verified "مُتحقَّق منها" "مُسجَّلة من مصدرها الأولي، مع مصدر منشأ التحقق."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مُتحقَّق منها"
* #reported-unverified "مُبلَّغ عنه، غير متحقَّق منه" "محفوظة كما أبلغت عنها الأسرة (primarySource false)؛ لا يحتسبها جدول التطعيم."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مُبلَّغ عنه، غير متحقَّق منه"
* #rejected "مرفوضة" "الشهادة ليست دليلًا على جرعة؛ تُسجَّل الخطوة والسبب."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مرفوضة"
* #not-read "لم تُقرأ" "تعذّرت قراءة أي شيء من رمز QR؛ تُعامَل البطاقة على أنها ورقية."
  * ^designation[0].language = #ar
  * ^designation[0].value = "لم تُقرأ"

CodeSystem: TrustDemoCodeMappingBasisAr
Id: TrustDemoCodeMappingBasis-ar
Title: "كيف حصلت جرعة مستوردة على رمزها في جدول التطعيم الوطني"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoCodeMappingBasis: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoCodeMappingBasis)
* ^language = #ar
* ^caseSensitive = true
* #concept-map "بواسطة ConceptMap الوطني" "لرمز المنتج لدى الجهة المُصدِرة رمز مكافئ في جدول التطعيم ضمن الخريطة الوطنية."
  * ^designation[0].language = #ar
  * ^designation[0].value = "بواسطة ConceptMap الوطني"
* #clinician-confirmed "مؤكَّد من الممارس السريري" "لم يكن في الخريطة أي مُدخل؛ أكّد الممارس السريري المكافئ، وأُضيف القرار إلى الخريطة."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مؤكَّد من الممارس السريري"
* #unmapped "غير مُطابَق" "لا يُعرف أي مكافئ؛ يُحفَظ رمز الجهة المُصدِرة كما هو ويُعرَض على أنه غير مُطابَق."
  * ^designation[0].language = #ar
  * ^designation[0].value = "غير مُطابَق"
* #not-imported "غير مستوردة" "لم يُتحقَّق من الجرعة، لذا لم تُستورَد ولم تُطابَق."
  * ^designation[0].language = #ar
  * ^designation[0].value = "غير مستوردة"

CodeSystem: TrustDemoVhlRefusalReasonAr
Id: TrustDemoVhlRefusalReason-ar
Title: "لماذا لم يُتح الرابط المُشارَك أي شيء"
Description: "ملحق باللغة العربية (ar) لنظام الرموز TrustDemoVhlRefusalReason: تسميات كل مفهوم. ترجمة غير رسمية أعدّها وكيل آلي، دون مراجعة بشرية."
* ^status = #draft
* ^experimental = true
* ^content = #supplement
* ^supplements = Canonical(TrustDemoVhlRefusalReason)
* ^language = #ar
* ^caseSensitive = true
* #withdrawn "مسحوب" "سحب الحامل الرابط قبل انتهاء صلاحيته."
  * ^designation[0].language = #ar
  * ^designation[0].value = "مسحوب"
* #expired "منتهية الصلاحية" "ورد الطلب بعد تاريخ انتهاء الصلاحية الذي اختاره الحامل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "منتهية الصلاحية"
* #wrong-passcode "رمز مرور خاطئ" "رمز المرور المُقدَّم لا يطابق الرمز الذي حدّده الحامل."
  * ^designation[0].language = #ar
  * ^designation[0].value = "رمز مرور خاطئ"
