# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import buttons, texts

# add import
from asyncio import create_task


async def contact_handler_task(message: Message, state: FSMContext):
    """
    Foydalanuvchi admin bilan bog'lanish uchun tugma
    """
    
    
    await message.answer(texts.CONTACT, reply_markup=buttons.BACK_MENU)
    
    
@dp.message_handler(lambda message: message.text.startswith((buttons.CONTACT)),state='*')
async def contact_handler(message: Message, state: FSMContext):
    await create_task(contact_handler_task(message, state))