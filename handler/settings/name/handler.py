# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services.services import getUser
from states.state import NameChange

# add import
from asyncio import create_task




async def settings_name_handler_task(message: Message, state: FSMContext):
    """
    Foydalanuvchi ismini o'zgartirish 
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    await message.answer(text=texts.NAME_CHANGE, reply_markup=buttons.ADD_BACK_BUTTON)
    
    await NameChange.name.set()
    
    
@dp.message_handler(lambda message: message.text.startswith((buttons.NAME_CHANGE)),state='*')
async def settings_name_handler(message: Message, state: FSMContext):
    await create_task(settings_name_handler_task(message, state))
    