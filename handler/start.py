# aiogram  import
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from services.services import getUser
from states.state import Register
from .menu import MainMenu

# add import
from asyncio import create_task



async def start_handler_task(message: Message, state: FSMContext):
    """
    start, /help commandalari uchun. Botga birichi kirgan userni anilash
    va uni ro'yxatdan o'rtkazishga jo'natish yoki ro'yxatdan  o'tgan userni
    asosiy menuga o'tqazish
    """
    
    user_id = message.from_user.id
    user = getUser(user_id)
    
    if not user:
        """
        Agar user ro'yxatdan o'tmagan bo'lsa
        uni ro'yxatdan o'tqaishga jo'natish
        """
        await message.answer(texts.REGISTER_NAME)
        await Register.name.set()
        return
    
    await MainMenu(message, state)    
    
@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    await create_task(start_handler_task(message, state))