# aiogram imports
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext

# loader import
from loader import dp
from states.state import Homeworks
from utils import texts, buttons

# add import
from asyncio import create_task


async def homeworks_get_task(message: Message, state: FSMContext):
    """
    Foydalanuvchining uyga vazifasini qabul qilish
    """

    document_id = message.document.file_id

    data = await state.get_data()

    if 'files' in data:
        data['files'].append(document_id)
    else:
        data['files'] = [document_id]

    await state.update_data(data)

    await message.answer(
        "Qabul qilindi",
        reply_markup=buttons.SEND_HOME_WORKS
    )


@dp.message_handler(content_types=ContentTypes.DOCUMENT, state=Homeworks.file)
async def homeworks_get(message: Message, state: FSMContext):
    await create_task(homeworks_get_task(message, state))
