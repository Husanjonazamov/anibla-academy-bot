# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import buttons, texts



@dp.message_handler(lambda message: message.text.endswith('🔒'), state='*')
async def locked_lesson_warning(message: Message, state: FSMContext):
    """
    Qulflangan dars bosilganda foydalanuvchiga ogohlantirish beradi.
    """
    await message.answer(texts.CLOSE_LESSONS)
    