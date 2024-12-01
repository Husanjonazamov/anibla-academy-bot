from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BACK = '🔙 Ortga'

BACK_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BACK)
        ]
    ],
    resize_keyboard=True
)


ADD_BACK = '🔙 Ortga'

CHECH_COUNTY = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(
        text='🤝 Rozilik berish va davom ettirish', callback_data='success_county')]
])

PAYMENT_BUTTONS = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [InlineKeyboardButton(text='💳 Sotib olish', url='')],
    [InlineKeyboardButton(text='🔙 Ortga', callback_data='back')]
])

ADD_BACK_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ADD_BACK)
        ]
    ],
    resize_keyboard=True
)


REGISTER_PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📲 Telefon raqamni yuborish',
                           request_contact=True)
        ]
    ],
    resize_keyboard=True
)


COURSE_SHOP = ['🛒 Kursni sotib olish']
COURSE_LIST = ['📖 Darsliklar']

CONTACT = "☎️ Bog'lanish"
SETTINGS = "⚙️ Sozlamalar"

MAIN_MENU_FOR_PREMIUM = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=COURSE_LIST[0]),
        ],
        [
            KeyboardButton(text=CONTACT),
            KeyboardButton(text=SETTINGS),
        ],
    ],
    resize_keyboard=True
)

MAIN_MENU_FOR_FREE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=COURSE_SHOP[0]),
        ],
        [
            KeyboardButton(text=CONTACT),
            KeyboardButton(text=SETTINGS),
        ],
    ],
    resize_keyboard=True
)


NAME_CHANGE = "Ismni o'zgartirish"
PHONE_CHANGE = "Telefon raqamni o'zgartirish"


SETTINGS_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NAME_CHANGE),
            KeyboardButton(text=PHONE_CHANGE),
        ],
        [
            KeyboardButton(text=BACK)
        ]
    ],
    resize_keyboard=True
)


HOME_WORKS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🏘 Uyga vazifa topshirish', callback_data='homeworks')
        ]
    ]
)

HOME_WORKS_DOWNLOAD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🎓📚 Uyga vazifani topshirish', callback_data='homeworks')
        ]
    ]
)

SEND_HOME_WORKS = ReplyKeyboardMarkup(
    keyboard=[
        ['✈️ Yuborish'],
        ['🔙 Ortga']
    ], resize_keyboard=True
)
