# aiogram import
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from states.state import Register
from services.services import createUser
from handler.menu import MainMenu

# add import
from asyncio import create_task



async def register_phone_task(message: Message, state: FSMContext):
    """
    Ro'yxatdan o'tmagan userni ro'yxatdan o'tqazishni boshlash va telefon raqamini olish
    """
    
    data = await state.get_data()
    name = data['name']
    user_id = message.from_user.id
    
    if message.content_type == 'contact':
        phone = message.contact.phone_number
    else:
        phone = message.text 

    await state.update_data({
        'user_id': user_id,
        'name': name,
        'phone': phone,
    })
    
    user = {
        'name': name,
        'phone': phone,
        'user_id': user_id 
    }
    
    createUser(user)
    await MainMenu(message, state)

@dp.message_handler(content_types=['text', 'contact'], state=Register.phone)
async def register_phone(message: Message, state: FSMContext):
    await create_task(register_phone_task(message, state))

