def chatbot_reply(user_input):
    dictionary = {
    "greeting": "أهلاً بيك في عيادة سمايل كير. اقدر اساعدك في المواعيد، الأسعار، الخدمات، أو الحجز.",
    
    "number": "تقدر تتواصل معانا على رقم 01012345678، أو واتساب على 01198765432.",
    
    "location": "العيادة موجودة في مدينة نصر، شارع عباس العقاد، بجوار جنينة مول. العنوان ده تجريبي للعرض فقط.",
    
    "working_hours": "مواعيد العيادة من السبت للخميس، من 12 الظهر لحد 10 بالليل. الجمعة إجازة.",
    
    "booking": "للحجز، ابعتلنا اسمك ورقم موبايلك والخدمة اللي محتاجها، وفريق الاستقبال هيتواصل معاك لتأكيد المعاد.",
    
    "consultation_price": "سعر الكشف التجريبي 300 جنيه، ولو عملت إجراء في نفس الزيارة ممكن يتم خصم الكشف حسب الحالة.",
    
    "cleaning_price": "تنظيف الجير وتلميع الأسنان بيبدأ من 600 جنيه، والسعر النهائي بيتحدد بعد الكشف حسب حالة الأسنان.",
    
    "whitening_price": "تبييض الأسنان بيبدأ من 2500 جنيه، والنتيجة بتختلف حسب لون الأسنان وحالتها قبل الجلسة.",
    
    "filling_price": "الحشو التجميلي بيبدأ من 800 جنيه للسن، والسعر بيختلف حسب حجم التسوس ونوع الحشو المطلوب.",
    
    "root_canal_price": "علاج العصب بيبدأ من 1800 جنيه للسن، والسعر بيختلف حسب عدد القنوات وحالة السن.",
    
    "implant_price": "زراعة الأسنان بتبدأ من 12000 جنيه للزرعة الواحدة، والسعر النهائي بيتحدد بعد الكشف والأشعة.",
    
    "braces_price": "تقويم الأسنان بيبدأ من 18000 جنيه، وبيتم تحديد الخطة والسعر بعد الكشف وتقييم الحالة.",
    
    "veneers_price": "الفينير أو ابتسامة هوليوود بتبدأ من 4500 جنيه للسن، وبيتم تحديد العدد المناسب بعد الكشف.",
    
    "children": "متاح علاج أسنان للأطفال، زي الكشف، الحشو، تنظيف الأسنان، وخلع الأسنان اللبنية عند الحاجة.",
    
    "emergency": "في حالات الطوارئ زي ألم شديد، تورم، كسر في السن، أو نزيف، يفضل التواصل مع العيادة فوراً على الواتساب.",
    
    "doctors": "العيادة فيها دكاترة متخصصين في الحشو التجميلي، علاج العصب، التركيبات، الزراعة، والتقويم.",
    
    "payment": "متاح الدفع كاش أو فودافون كاش، وبعض الخدمات ممكن تتقسم على دفعات حسب الخطة العلاجية.",
    
    "offers": "حالياً عندنا عرض تجريبي: كشف + تنظيف جير بسعر 750 جنيه بدل 900 جنيه. العرض ده لغرض الديمو فقط.",
    
    "thanks": "العفو، تحت أمرك في أي وقت."
}


def chatbot_reply(user_input):
    dictionary = {
    "greeting": "أهلاً بيك في عيادة سمايل كير. اقدر اساعدك في المواعيد، الأسعار، الخدمات، أو الحجز.",
    
    "number": "تقدر تتواصل معانا على رقم 01012345678، أو واتساب على 01198765432.",
    
    "location": "العيادة موجودة في مدينة نصر، شارع عباس العقاد، بجوار جنينة مول. العنوان ده تجريبي للعرض فقط.",
    
    "working_hours": "مواعيد العيادة من السبت للخميس، من 12 الظهر لحد 10 بالليل. الجمعة إجازة.",
    
    "booking": "للحجز، ابعتلنا اسمك ورقم موبايلك والخدمة اللي محتاجها، وفريق الاستقبال هيتواصل معاك لتأكيد المعاد.",
    
    "consultation_price": "سعر الكشف التجريبي 300 جنيه، ولو عملت إجراء في نفس الزيارة ممكن يتم خصم الكشف حسب الحالة.",
    
    "cleaning_price": "تنظيف الجير وتلميع الأسنان بيبدأ من 600 جنيه، والسعر النهائي بيتحدد بعد الكشف حسب حالة الأسنان.",
    
    "whitening_price": "تبييض الأسنان بيبدأ من 2500 جنيه، والنتيجة بتختلف حسب لون الأسنان وحالتها قبل الجلسة.",
    
    "filling_price": "الحشو التجميلي بيبدأ من 800 جنيه للسن، والسعر بيختلف حسب حجم التسوس ونوع الحشو المطلوب.",
    
    "root_canal_price": "علاج العصب بيبدأ من 1800 جنيه للسن، والسعر بيختلف حسب عدد القنوات وحالة السن.",
    
    "implant_price": "زراعة الأسنان بتبدأ من 12000 جنيه للزرعة الواحدة، والسعر النهائي بيتحدد بعد الكشف والأشعة.",
    
    "braces_price": "تقويم الأسنان بيبدأ من 18000 جنيه، وبيتم تحديد الخطة والسعر بعد الكشف وتقييم الحالة.",
    
    "veneers_price": "الفينير أو ابتسامة هوليوود بتبدأ من 4500 جنيه للسن، وبيتم تحديد العدد المناسب بعد الكشف.",
    
    "children": "متاح علاج أسنان للأطفال، زي الكشف، الحشو، تنظيف الأسنان، وخلع الأسنان اللبنية عند الحاجة.",
    
    "emergency": "في حالات الطوارئ زي ألم شديد، تورم، كسر في السن، أو نزيف، يفضل التواصل مع العيادة فوراً على الواتساب.",
    
    "doctors": "العيادة فيها دكاترة متخصصين في الحشو التجميلي، علاج العصب، التركيبات، الزراعة، والتقويم.",
    
    "payment": "متاح الدفع كاش أو فودافون كاش، وبعض الخدمات ممكن تتقسم على دفعات حسب الخطة العلاجية.",
    
    "offers": "حالياً عندنا عرض تجريبي: كشف + تنظيف جير بسعر 750 جنيه بدل 900 جنيه. العرض ده لغرض الديمو فقط.",
    
    "thanks": "العفو، تحت أمرك في أي وقت." }
    user_input = str(user_input).lower().strip()

    arabic_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهويأإآةىؤئ"
    english_letters = "abcdefghijklmnopqrstuvwxyz"

    arFlag = False
    engFlag = False

    for letter in user_input:
        if letter in arabic_letters:
            arFlag = True
        elif letter in english_letters:
            engFlag = True

    if engFlag or not arFlag:
        return "معلش، أنا بفهم عربي بس. ممكن تكتب سؤالك بالعربي؟"

    for key in dictionary:

        if key == "greeting" and (
            "اهلا" in user_input
            or "أهلا" in user_input
            or "السلام عليكم" in user_input
            or "هاي" in user_input
            or "هالو" in user_input
            or "مرحبا" in user_input
            or "ازيك" in user_input
            or "إزيك" in user_input
            or "عامل ايه" in user_input
            or "صباح الخير" in user_input
            or "مساء الخير" in user_input
        ):
            return dictionary.get(key)

        elif key == "number" and (
            "رقم" in user_input
            or "النمرة" in user_input
            or "نمره" in user_input
            or "موبايل" in user_input
            or "تليفون" in user_input
            or "تلفون" in user_input
            or "واتساب" in user_input
            or "اتواصل" in user_input
            or "اكلمكم" in user_input
        ):
            return dictionary.get(key)

        elif key == "location" and (
            "فين" in user_input
            or "مكان" in user_input
            or "العنوان" in user_input
            or "عنوان" in user_input
            or "موجودين فين" in user_input
            or "العيادة فين" in user_input
            or "مكانكم" in user_input
        ):
            return dictionary.get(key)

        elif key == "working_hours" and (
            "مواعيد" in user_input
            or "المواعيد" in user_input
            or "بتفتحوا" in user_input
            or "بتقفلوا" in user_input
            or "فاتحين" in user_input
            or "شغالين" in user_input
            or "امتى" in user_input
            or "إمتى" in user_input
            or "الساعة كام" in user_input
            or "الساعه كام" in user_input
        ):
            return dictionary.get(key)

        elif key == "booking" and (
            "احجز" in user_input
            or "حجز" in user_input
            or "عايز احجز" in user_input
            or "عايزة احجز" in user_input
            or "ميعاد" in user_input
            or "معاد" in user_input
            or "موعد" in user_input
            or "أحجز" in user_input
        ):
            return dictionary.get(key)

        elif key == "consultation_price" and (
            "كشف" in user_input
            or "سعر الكشف" in user_input
            or "الكشف بكام" in user_input
            or "كشف بكام" in user_input
            or "استشارة" in user_input
            or "استشاره" in user_input
        ):
            return dictionary.get(key)

        elif key == "cleaning_price" and (
            "تنظيف" in user_input
            or "جير" in user_input
            or "تلميع" in user_input
            or "تنضيف" in user_input
            or "تنظيف الجير" in user_input
        ):
            return dictionary.get(key)

        elif key == "whitening_price" and (
            "تبييض" in user_input
            or "تبيض" in user_input
            or "تفتيح" in user_input
            or "اسناني تبقى بيضا" in user_input
            or "أسناني تبقى بيضا" in user_input
        ):
            return dictionary.get(key)

        elif key == "filling_price" and (
            "حشو" in user_input
            or "الحشو" in user_input
            or "تسوس" in user_input
            or "حشو تجميلي" in user_input
            or "سوسة" in user_input
            or "سوسه" in user_input
        ):
            return dictionary.get(key)

        elif key == "root_canal_price" and (
            "عصب" in user_input
            or "علاج عصب" in user_input
            or "حشو عصب" in user_input
            or "العصب" in user_input
            or "الم شديد" in user_input
            or "ألم شديد" in user_input
        ):
            return dictionary.get(key)

        elif key == "implant_price" and (
            "زراعة" in user_input
            or "زراعه" in user_input
            or "زرعة" in user_input
            or "زرعه" in user_input
            or "زرعات" in user_input
            or "سن ناقص" in user_input
            or "ضرس ناقص" in user_input
        ):
            return dictionary.get(key)

        elif key == "braces_price" and (
            "تقويم" in user_input
            or "التقويم" in user_input
            or "اعوجاج" in user_input
            or "أسناني مش مظبوطة" in user_input
            or "اسناني مش مظبوطة" in user_input
        ):
            return dictionary.get(key)

        elif key == "veneers_price" and (
            "فينير" in user_input
            or "فينيرز" in user_input
            or "ابتسامة هوليوود" in user_input
            or "هوليود سمايل" in user_input
            or "قشور" in user_input
            or "تركيبات تجميلية" in user_input
        ):
            return dictionary.get(key)

        elif key == "children" and (
            "اطفال" in user_input
            or "أطفال" in user_input
            or "طفل" in user_input
            or "ابني" in user_input
            or "بنتي" in user_input
            or "للاطفال" in user_input
            or "للأطفال" in user_input
        ):
            return dictionary.get(key)

        elif key == "emergency" and (
            "طوارئ" in user_input
            or "وجع جامد" in user_input
            or "ألم جامد" in user_input
            or "الم جامد" in user_input
            or "تورم" in user_input
            or "وارم" in user_input
            or "نزيف" in user_input
            or "كسر" in user_input
        ):
            return dictionary.get(key)

        elif key == "doctors" and (
            "الدكاترة" in user_input
            or "الدكتور" in user_input
            or "دكتور" in user_input
            or "تخصصات" in user_input
            or "متخصصين" in user_input
            or "مين الدكتور" in user_input
        ):
            return dictionary.get(key)

        elif key == "payment" and (
            "دفع" in user_input
            or "الدفع" in user_input
            or "كاش" in user_input
            or "فيزا" in user_input
            or "فودافون كاش" in user_input
            or "تقسيط" in user_input
            or "اقسط" in user_input
            or "أقسط" in user_input
        ):
            return dictionary.get(key)

        elif key == "offers" and (
            "عرض" in user_input
            or "عروض" in user_input
            or "خصم" in user_input
            or "تخفيض" in user_input
            or "في خصومات" in user_input
            or "فيه خصومات" in user_input
        ):
            return dictionary.get(key)

        elif key == "thanks" and (
            "شكرا" in user_input
            or "شكرًا" in user_input
            or "متشكر" in user_input
            or "متشكرة" in user_input
            or "تسلم" in user_input
            or "ميرسي" in user_input
        ):
            return dictionary.get(key)

    return "مش متأكد من إجابة السؤال ده حالياً. ممكن تسألني عن المواعيد، الأسعار، الحجز، المكان، أو طرق التواصل."