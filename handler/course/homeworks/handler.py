# aiogram import
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import buttons, texts
from states.state import Homeworks

# add import
from asyncio import create_task


async def homeworks_handler_task(callback: CallbackQuery, state: FSMContext):
    """
    Uyga vazifa topshirishni bosh funksiyasi
    """

    await callback.message.answer(texts.HOMEWORKS_SET, reply_markup=buttons.BACK_MENU)

    await Homeworks.file.set()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'homeworks')
async def homeworks_handler(callback: CallbackQuery, state: FSMContext):
    await create_task(homeworks_handler_task(callback, state))
