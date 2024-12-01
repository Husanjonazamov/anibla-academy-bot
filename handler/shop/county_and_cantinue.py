from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

from services.services import generate_payment
from utils import texts, buttons
from utils.env import COURSE_PRICE


@dp.callback_query_handler(lambda c: c.data == 'success_county', state='*')
async def shop_func(callback_query: types.CallbackQuery, state: FSMContext):

    user_id = callback_query.from_user.id

    payment = generate_payment(amount=COURSE_PRICE, user_id=user_id)

    markup = buttons.PAYMENT_BUTTONS
    markup.inline_keyboard[0][0].url = payment['url']

    await callback_query.message.edit_caption(
        caption=texts.COURSE_INFO,
        reply_markup=markup)
