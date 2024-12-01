# aiogram import
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext


# kode import
from loader import dp
from utils import texts, buttons
from .menu import MainMenu

    

@dp.message_handler(lambda message: message.text.startswith((buttons.BACK)), state='*')
async def back_handler(message: Message, state: FSMContext):
    await MainMenu(message, state)

@dp.callback_query_handler(lambda c:c.data=='back', state='*')
async def create_task(callback_query: CallbackQuery, state: FSMContext):
    callback_query.message.from_user.id = callback_query.from_user.id    
    await MainMenu(callback_query.message, state)