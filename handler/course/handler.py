from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext

# Importlar
from loader import dp
from utils import buttons, texts
from services.services import get_lessons

async def list_lessons_task(message: Message, state: FSMContext):
    """
    Asosiy darslarni olib tugma ko'rinishida chiqarib beradigan funksiya.
    1-dars va `is_access=True` bo'lgan darslar ochiq, qolganlari qulflangan.
    """
    user_id = message.from_user.id
    lessons = get_lessons(user_id)  

    if lessons:
        course_lessons = ReplyKeyboardMarkup(resize_keyboard=True)
        row = []
        for index, lesson in enumerate(lessons):
            lesson_id = lesson['id']
            lesson_name = f"{lesson_id}-dars"

            if lesson_id == 1 or lesson.get('is_access', False):  
                button_text = lesson_name
            else:
                button_text = f"{lesson_name} 🔒"

            row.append(KeyboardButton(text=button_text))
            if (index + 1) % 3 == 0:
                course_lessons.add(*row)
                row = []
        if row:
            course_lessons.add(*row)

        course_lessons.add(KeyboardButton(text=buttons.BACK))
        
        await message.answer(texts.COURSE_LESSONS, reply_markup=course_lessons)
    else:
        await message.answer(texts.NOT_COURSE)



@dp.message_handler(lambda message: message.text == '📖 Darsliklar' or \
                                    message.text.startswith('⏭️ Davom etish'), state='*')
async def list_lessons(message: Message, state: FSMContext):
    await list_lessons_task(message, state)
