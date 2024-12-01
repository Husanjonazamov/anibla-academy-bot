
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.env import ADMIN_ID


@dp.message_handler(content_types=types.ContentType.PHOTO, state='*')
async def send_video(message: types.Message, state=FSMContext):

    if message.from_user.id == ADMIN_ID:
        file_id = message.photo[-1].file_id
        await message.answer(file_id)
