
SEND_HOME_WORKS_SUCCESS = \
    """
<b>
Homework muvaffaqiyatli yuborildi!
</b>
"""

SHARTNOMA_INFO = """
<b>
Ushbu kursda siz Dublyajni, hamda aktyorlik mahoratingizni oshirasiz ! 

Hamda Aniblauz dublyaj jamoasiga qo'shilish imkoniyatingiz bo‘ladi.
</b>
"""

COURSE_INFO = """
Narxi: 330 000 UZS
Amal qilish muddati: 1 yil
To‘lovdan so‘ng, kursimiz siz uchun ochiladi !
"""

DISCLEMER = """
⚠️ Iltimos shartnomani diqqat bilan o'qib chiqing
"""

PHONE = \
    """
Iltimos telefon raqamingizni kiritish yoki pastdagi <b>📲 Telefon raqamni yuborish</b> degan tugmani bosing!
"""

REGISTER_NAME = \
    """
<b>
Ismingizni kiriting!
</b>
"""

MENU = \
    """
<b>
Asosiy menyu
</b>
"""

SETTINGS_MESSAGE = \
    """
<b>
Ma'lumotlarni o'zgartirish uchun quyidagi tugmalardan foydalanishingiz mumkin.
</b>
"""


NAME_CHANGE = \
    """
<b>
Ismingizni kiriting!
</b>
"""


PHONE_CHANGE = \
    """
<b>
Telefon raqamingizni kiriting!
</b>
"""


NAME_UPDATE_SUCCESS = \
    """
<b>
✅ Ism muffaqiyatli almashtirildi
</b>
"""

PHONE_UPDATE_SUCCESS = \
    """
<b>
✅ Telefon raqam muffaqiyatli almashtirildi
</b>
"""


CONTACT = \
    """
Telefon: +998 94 001 47 41
telegram: @HusanjonAzamov
"""


COURSE_LESSONS = \
"""
<strong>🎓 Darsni tanlang:</strong>

📚 Hozirda faqat birinchi dars ochiq. Darsni tugatganingizdan so'ng, ma'lum bir vaqtdan so'ng yangi dars ochiladi. 

🔒 Har bir yangi dars uchun qulf mavjud, kerakli vaqt o'tgandan  keyingi darsni olish imkoniyatingiz bo'ladi. 

👇 Quyidagi darsni boshlash uchun bosing!
"""


NOT_COURSE = \
"""
darslar mavjud emas
"""



CLOSE_LESSONS = """
🔒 Bu dars hozirda yopiq. Iltimos belgilangan vaqtni kuting
"""


HOMEWORKS_SET = \
"""
📚 <b>Uyga vazifangizni fayl ko'rinishida yuboring:</b>
"""


HOMEWORK_ALREADY = """
⚠️ <b>Vazifani ikkinchi marotaba yuborishga urinyapsiz!</b>
Iltimos, faqat bir marta yuboring.
"""


HOMEWORK_SUCCESS = \
"""
✅ <b>Qabul qilindi! Uyga vazifani yuborish uchun <i> ✈️ Yuborish </i>  tugmasini bosing.
</b>
"""

def lessons(**kwargs):
    lessons_text = ''

    lessons_text += f"{kwargs['title']}\n\n"
    lessons_text += f"{kwargs['description']}\n\n"
    lessons_text += f"{kwargs['date']}\n"

    return lessons_text



CHANNEL_REQUEST = \
"""
📢 Hurmatli foydalanuvchi!

Siz ushbu kursni to'liq ko'rish huquqiga ega bo'lish uchun, bizning rasmiy Telegram kanalimizga majburiy obuna bo'lishingiz kerak. Kanalga obuna bo'lish orqali siz nafaqat kurs materiallariga kirish imkoniyatiga ega bo'lasiz, balki yangiliklar, foydali maslahatlar va boshqa eksklyuziv ma'lumotlardan ham xabardor bo'lib turasiz!

Kanalga obuna bo'lganingizdan so'ng, "Tekshirish" tugmasini bosing.

Rahmat! 😊
"""




CHANNEL_ERROR = \
"""
<b>
❌ Siz hali hamma kanallarga obuna bo'lmadingiz. Iltimos, quyidagi kanallarga obuna bo'ling
</b>
"""