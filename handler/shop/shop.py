from aiogram  import types
from aiogram.dispatcher import FSMContext
from loader import dp

from utils.env import SHARTNOMA_FILE_ID
from utils import texts, buttons

@dp.message_handler(text=buttons.COURSE_SHOP[0])
async def shop_func(message:types.Message, state:FSMContext):

    await message.answer(
        text=texts.DISCLEMER,
        reply_markup=types.ReplyKeyboardRemove()
    )
    
    await message.answer_document(
        document=SHARTNOMA_FILE_ID,
        caption=texts.SHARTNOMA_INFO,
        reply_markup=buttons.CHECH_COUNTY
    )