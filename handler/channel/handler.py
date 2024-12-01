# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext

# kode import
from handler.channel.sub import check_subscriptions
from utils import texts, buttons
from loader import bot, dp

# add import
import logging
from asyncio import create_task
from aiogram.types import Message


async def check_subscriptions_callback(call: types.CallbackQuery, state: FSMContext):

    """
    kannalarga obunani tekshirishi
    """
    user_id = call.from_user.id
    not_subscribed = await check_subscriptions(bot, user_id)

    if not not_subscribed:
        await call.message.delete()
        await call.message.answer(
            text=texts.MENU,
            reply_markup=buttons.MAIN_MENU_FOR_PREMIUM
        )
    else:
        await call.message.delete()
        keyboard = buttons.get_subscription_buttons(not_subscribed)
        await call.message.answer(texts.CHANNEL_ERROR, reply_markup=keyboard)



@dp.callback_query_handler(lambda callbask_query: callbask_query.data.startswith("check_subscriptions"), state="*")
async def check(call: types.CallbackQuery, state: FSMContext):
  await create_task(check_subscriptions_callback(call, state))
  
  