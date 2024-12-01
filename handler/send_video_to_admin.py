
from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.env import ADMIN_ID

from loader import dp


@dp.message_handler(content_types=types.ContentType.VIDEO, state='*')
async def send_video(message: types.Message, state=FSMContext):
    if message.from_user.id == ADMIN_ID:
        video_id = message.video.file_id
        await message.answer(video_id)
