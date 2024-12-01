
from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.env import ADMIN_ID

from loader import dp


@dp.message_handler(content_types=types.ContentType.VOICE, state='*')
async def send_video(message: types.Message, state=FSMContext):

    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        file_id = message.voice.file_id
        await message.answer(file_id)
