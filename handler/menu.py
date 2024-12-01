# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext

# kode import
from services.services import getUser
from utils import buttons, texts
from loader import dp

@dp.message_handler(content_types=['video'])
async def MainMenu(message: types.Message, state: FSMContext):
    """
    Ro'yxatdan o'tgan userlar uchun asosiy menu
    """
    user = getUser(user_id=message.from_user.id)
    
    if (user['is_purchased'] == True):
        await message.answer(
            text=texts.MENU,
            reply_markup=buttons.MAIN_MENU_FOR_PREMIUM
        )
    elif (user['is_purchased'] == False):
        await message.answer(
            text=texts.MENU,
            reply_markup=buttons.MAIN_MENU_FOR_FREE
        )

    await state.finish()