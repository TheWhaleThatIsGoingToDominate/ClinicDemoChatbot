import uuid #new 
user_states = {}
databaseServices = {}


def chatbot_reply(session_id, user_input):
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
    
    "thanks": "العفو، تحت أمرك في أي وقت.",
    
    "booking": "تمام، تقدر تحجز معانا بسهولة. ابعت اسمك، رقم موبايلك، والخدمة اللي محتاجها، وفريق العيادة هيتواصل معاك لتأكيد المعاد." }
    user_input = str(user_input).lower().strip()
    user_state = user_states.setdefault(session_id, {"FlagToBook":False})
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

    if user_state["FlagToBook"]:
        user_booking(user_input)
        user_state["FlagToBook"] = False
        return "تم استلام بيانات الحجز، وفريق العيادة هيتواصل معاك لتأكيد المعاد."

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

        elif key == "booking" and ( #BOOKING HEREEEEEEEEEEEEEEEEEE
            "احجز" in user_input
            or "حجز" in user_input
            or "عايز احجز" in user_input
            or "عايزة احجز" in user_input
            or "ميعاد" in user_input
            or "معاد" in user_input
            or "موعد" in user_input
            or "أحجز" in user_input
        ):
            user_state["FlagToBook"] = True
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

        #BOOKING HEREEEEEEEEEEEEEEEEEEEEEE
        elif key == "booking" and (
        "حجز" in user_input
        or "احجز" in user_input
        or "أحجز" in user_input
        or "عايز احجز" in user_input
        or "عايزة احجز" in user_input
        or "عاوز احجز" in user_input
        or "ميعاد" in user_input
        or "معاد" in user_input
        or "موعد" in user_input
        or "اقابل الدكتور" in user_input
        or "أقابل الدكتور" in user_input
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


# get the number of the client, then in databaseNumbers.update({number:name of client})
# then we make the value of the key of databaseNumbers the key of databaseServices, 
# its value is a tuple, representing the name, number, and the service that the user wants



arabic_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهويأإآةىؤئ"

arFlag = False


#idea: update the user input so that we remove the things that the functions already assessed, 
# and then put that in a global var to pass to the other function
#another idea: make databaseServices the one and only collection you will use, just make the number the key and make a small dict
#the value of the key, the small dict has the phonenumber, the name, and the wanted service.

def takingNumber(user_input):
    """will take the number of the user here, this function is dedicated to doing that"""
    user_input = str(user_input).lower().strip()
    check = user_input.split()
    for i in range(len(check)):
        if not(check[i].isdigit()):
            pass
        else:
            if len(check[i]) not in (10, 11):
                print("please e nter a valid phone number consisting of 11 digits")
            else:
                number = check[i]
                databaseServices.update({number:{"number":number}})#the job of the function
                check.remove(check[i])
                user_input = " ".join(check)
                return number,user_input
    
    raise TypeError(
    "please enter your phone number"
    )

    
    


#idea: make a function that helps takingName to diffrentitate between service and name
#my response to this idea: just make the flow like this:
# takingNumber >> takingService >> takingName



def takingService(number, user_input):
    """we will validate the service the user wants in this function, and then update the dictionary"""
    user_input = str(user_input).lower().strip()
    service_keywords = {
    "خلع ضرس عقل": [
        "خلع ضرس العقل",
        "خلع ضرس عقل",
        "ضرس العقل مدفون",
        "ضرس عقل مدفون",
        "ضرس العقل مطمور",
        "ضرس عقل مطمور",
        "ضرس العقل",
        "ضرس عقل"
    ],

    "حشو تجميلي": [
        "حشو للسن الأمامي",
        "حشو للسن الامامي",
        "حشو بلون السن",
        "حشو لون السن",
        "حشو كومبوزيت",
        "حشو تجميلي",
        "حشو أبيض",
        "حشو ابيض",
        "حشو قدام",
        "كومبوزيت"
    ],

    "تقويم شفاف": [
    "تقويم شفاف",
    "تقويم متحرك",
    "قوالب شفافة",
    "قوالب شفافه",
    "إنفزلاين",
    "انفزلاين"
    ],

    "تنظيف جير": [
        "تنظيف الأسنان",
        "تنظيف الاسنان",
        "تلميع الأسنان",
        "تلميع الاسنان",
        "إزالة الجير",
        "ازالة الجير",
        "تنظيف جير",
        "تنضيف جير",
        "شيل الجير",
        "إشيل الجير",
        "تنظيف",
        "تنضيف",
        "تلميع",
        "جير"
    ],

    "تبييض أسنان": [
        "عايزة أسناني تبيض",
        "عايزة اسناني تبيض",
        "عايز أسناني تبيض",
        "عايز اسناني تبيض",
        "تبييض الأسنان",
        "تبييض الاسنان",
        "تفتيح الأسنان",
        "تفتيح الاسنان",
        "اسناني تبقى بيضا",
        "أسناني تبقى بيضا",
        "ابتسامة أفتح",
        "ابتسامه افتح",
        "تبييض",
        "تبيض",
        "تفتيح"
    ],

    "علاج عصب": [
        "تنظيف العصب",
        "التهاب عصب",
        "العصب ملتهب",
        "سحب العصب",
        "علاج عصب",
        "حشو عصب",
        "سحب عصب",
        "وجع عصب",
        "ألم عصب",
        "الم عصب",
        "العصب",
        "عصب"
    ],

    "زراعة أسنان": [
        "زراعة أسنان",
        "زراعة اسنان",
        "تعويض ضرس",
        "تعويض سن",
        "ضرس ناقص",
        "سن ناقص",
        "زرع ضرس",
        "زرع سن",
        "زرعات",
        "زراعة",
        "زراعه",
        "زرعة",
        "زرعه"
    ],

    "أسنان أطفال": [
        "دكتور أطفال",
        "دكتور اطفال",
        "أسنان أطفال",
        "اسنان اطفال",
        "اسنان لبنيه",
        "سنان لبنية",
        "خلع سن لبني",
        "حشو طفل",
        "أطفال",
        "اطفال",
        "طفلة",
        "طفله",
        "طفل",
        "ابني",
        "بنتي"
    ],

    "علاج لثة": [
        "اللثة بتنزف",
        "اللثه بتنزف",
        "التهاب اللثة",
        "التهاب اللثه",
        "نزيف اللثة",
        "نزيف اللثه",
        "انحسار اللثة",
        "انحسار اللثه",
        "جيوب لثوية",
        "جيوب لثويه",
        "علاج لثة",
        "علاج لثه",
        "لثة",
        "لثه"
    ],

    "أشعة أسنان": [
        "أشعة على الضرس",
        "اشعة على الضرس",
        "أشعة على السن",
        "اشعة على السن",
        "أشعة بانوراما",
        "اشعة بانوراما",
        "أشعة أسنان",
        "اشعة اسنان",
        "بانوراما",
        "أشعة",
        "اشعة"
    ],

    "طوارئ أسنان": [
        "كسر في الضرس",
        "كسر في السن",
        "ضرس مكسور",
        "سن مكسور",
        "وقعت على سني",
        "خبطت سني",
        "وجع شديد",
        "وجع جامد",
        "ألم شديد",
        "الم شديد",
        "طوارئ",
        "تورم",
        "وارم",
        "خراج",
        "نزيف"
    ],

    "طقم أسنان": [
        "تركيبة متحركة",
        "تركيبه متحركه",
        "أسنان متحركة",
        "اسنان متحركه",
        "طقم أسنان",
        "طقم اسنان",
        "طقم كامل",
        "طقم جزئي"
    ],

    "تركيبات": [
        "جسر أسنان",
        "جسر اسنان",
        "تركيب ضرس",
        "تركيب سن",
        "طربوش ضرس",
        "طربوش سن",
        "تركيبات",
        "تركيبة",
        "تركيبه",
        "كراون",
        "طربوش",
        "كوبري",
        "تاج"
    ],

    "فينير": [
    "قشور تجميلية",
    "قشور تجميليه",
    "ابتسامة هوليود",
    "ابتسامه هوليود",
    "هوليود سمايل",
    "عدسات أسنان",
    "عدسات الاسنان",
    "فينيرز",
    "فينير",
    "قشور"
    ],

    "حشو عادي": [
        "الضرس فيه تسوس",
        "السن فيه تسوس",
        "الضرس مسوس",
        "السن مسوس",
        "حشو عادي",
        "حشو ضرس",
        "حشو سن",
        "عندي تسوس",
        "تسوس",
        "سوسة",
        "سوسه",
        "حشو"
    ],

    "خلع": [
        "عايزة اخلع",
        "عايز اخلع",
        "عاوز اخلع",
        "خلع ضرس",
        "خلع سن",
        "شيل الضرس",
        "شيل السن",
        "أخلع",
        "اخلع",
        "خلع"
    ],

    "تقويم": [
        "فراغات بين الأسنان",
        "فراغات بين الاسنان",
        "اعوجاج الأسنان",
        "اعوجاج الاسنان",
        "الأسنان معوجة",
        "الاسنان معوجه",
        "اسناني مش مظبوطة",
        "أسناني مش مظبوطة",
        "تزاحم الأسنان",
        "تزاحم الاسنان",
        "بروز الأسنان",
        "بروز الاسنان",
        "تقويم أسنان",
        "تقويم اسنان",
        "تقويم"
    ],

    "كشف": [
        "عايزة اكشف",
        "عايز اكشف",
        "عاوز اكشف",
        "استشارة",
        "استشاره",
        "أكشف",
        "اكشف",
        "أفحص",
        "افحص",
        "فحص",
        "كشف"
    ]
}
    
    #TODO: Make the function take the service the user wanted, remove it from the original user input, and then put it in the dict
    #TODO: Make the function (or the chatbot generally speaking) ask for comfirmation when the user inputted the service he wanted

    txt = ""
    txtToRemove = ""
    FlagToBreakOuterForLoop = False
    for service, keywords in service_keywords.items(): 
        for keyword in keywords:
            if keyword in user_input: # exact matching may miss typos and spelling variations, can be countered by passing in dict values
                txtToRemove += keyword
                txt += f"{service} ({keyword})"
                FlagToBreakOuterForLoop = True
                break
            else:
                pass
        if FlagToBreakOuterForLoop == True:

            break
    if not FlagToBreakOuterForLoop:
        raise TypeError( "الخدمة مش واضحة، من فضلك اكتب الخدمة المطلوبة." )
            
    
    databaseServices[number].update({"service":txt})
    
    #removing the service from the user input
    user_input = user_input.split()
    txtToRemove = txtToRemove.split()
    for theWord in txtToRemove:
        user_input.remove(theWord)
    user_input = " ".join(user_input)

    return number, user_input


def takingName(number, user_input): 
    """we will take care of the name of the user here, this function has to work for the 
    takingNumber function to save the number to the dict
    some examples you will have to take care of: jumana sameh, mostafa mahmoud (2 names having a space between them)"""
    user_input = str(user_input).lower().strip()
    check = user_input.split()
    name = ""
    
    for i in range(len(check)):
        if check[i] == "" : #empty name
            print("please input your name")
            raise TypeError
        else: 
            if not check[i].isalpha(): #random numbers and symbols
                print("invalid name, must not contain random numbers or symbols")
                raise TypeError
            else:
                if not 2 < len(check[i]) < 15: #checking if the name is within range
                    print("invalid name")
                    raise TypeError
                else:
                    name += check[i] + " "
    name = name.rstrip()
    for word in name.split():
        check.remove(word)
    
    databaseServices[number].update({"name":name})#the job of the function
    user_input = " ".join(check)
    



def user_booking(user_input):
    """uses all pervious functions to gather the info and append it to databaseServices dict"""
    takingnumber = takingNumber(user_input)
    takingservice = takingService(*takingnumber)
    takingName(*takingservice)
    print("BOOKING SAVED:", databaseServices)
    pass