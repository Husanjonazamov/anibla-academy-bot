# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services.services import getUser, changeName
from states.state import NameChange

# add import
from asyncio import create_task
import logging  # Xatolarni kuzatish uchun logging


async def settings_name_update_task(message: Message, state: FSMContext):
    """
    Foydalanuvchi ismini kiritish uchun kod
    """
    
    user_id = message.from_user.id
    
    user = getUser(user_id)
    
    # Foydalanuvchining yangi ismini olish
    name = message.text
    await state.update_data({
        'name': name
    })
    
    # Foydalanuvchi ismini yangilash
    user = changeName(user_id, name)

    await message.answer(text=texts.NAME_UPDATE_SUCCESS, reply_markup=buttons.SETTINGS_MENU)
    
    # State ni tugatish
    await state.finish()
    

@dp.message_handler(content_types=['text'], state=NameChange.name)
async def settings_name_update(message: Message, state: FSMContext):
    if message.text in [buttons.ADD_BACK]:
        await message.answer(text=texts.SETTINGS_MESSAGE, reply_markup=buttons.SETTINGS_MENU)
        await state.finish()
    else:
        await create_task(settings_name_update_task(message, state))
