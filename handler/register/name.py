# aiogram import
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext


# kode import
from loader import dp
from utils import texts, buttons
from states.state import Register

# add import
from asyncio import create_task


async def register_name_task(message: Message, state: FSMContext):
    """
    Ro'yxatdan o'tmagan userni ro'yxatdan o'tqazishni boshlash va ismini olish
    """
    
    name = message.text
    
    
    await state.set_data({
        'name': name
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.REGISTER_PHONE)
    
    await Register.phone.set()
    
    
@dp.message_handler(content_types=ContentTypes.TEXT, state=Register.name)
async def register_name(message: Message, state: FSMContext):
    await create_task(register_name_task(message, state))