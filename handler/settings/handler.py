# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services.services import getUser

# add import
from asyncio import create_task




async def settings_handler_task(message: Message, state: FSMContext):
    """
    Foydalanuvchi malumotlarni o'zgartirish uchun sozlamalar bo'limi
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    await message.answer(text=texts.SETTINGS_MESSAGE, reply_markup=buttons.SETTINGS_MENU)
    
    
    
@dp.message_handler(lambda message: message.text.startswith((buttons.SETTINGS)),state='*')
async def settings_handler(message: Message, state: FSMContext):
    await create_task(settings_handler_task(message, state))
    