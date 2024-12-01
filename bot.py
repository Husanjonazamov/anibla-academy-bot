# aiogram import
from aiogram import executor

# kode import
from loader import dp, bot
from utils.env import ADMIN_ID
import handler  # noqa: F401


async def on_startup(dispatcher):
    """
    Botni asosiy ishga tushiradigan file
    """

    await bot.send_message(ADMIN_ID, 'bot ishga tushdi')

executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
