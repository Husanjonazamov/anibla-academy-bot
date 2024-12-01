# aiogram imports
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

# loader import
from handler.menu import MainMenu
from loader import dp
from services.services import post_homeworks
from states.state import Homeworks
from utils import texts, buttons

# add import
from asyncio import create_task


async def homeworks_get_task(message: Message, state: FSMContext):
    """
    Foydalanuvchining uyga vazifasini qabul qilish
    """
    data = await state.get_data()
    files = data['files']
    user_id = message.from_user.id

    response = post_homeworks(data['lesson_id'], user_id, files)
    print("🚀 ~ response:", response)

    await message.answer(text=texts.SEND_HOME_WORKS_SUCCESS)

    await MainMenu(message, state)


@dp.message_handler(text='✈️ Yuborish', state=Homeworks.file)
async def homeworks_get(message: Message, state: FSMContext):
    await create_task(homeworks_get_task(message, state))
