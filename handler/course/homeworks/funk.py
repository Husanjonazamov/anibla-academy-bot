# loader import
from loader import dp, bot

# add import
from utils.env import BOT_TOKEN
import os
import requests


async def download_file(document):
    """
    Telegram'dan kelgan faylni yuklab olish va 'down' papkasiga saqlash.
    """
    # Fayl haqida ma'lumot olish
    file_info = await bot.get_file(document.file_id)
    file_path = file_info.file_path

    # Faylni yuklab olish uchun URL
    file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

    # Faylni 'down' papkasiga saqlash
    download_dir = "down"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    local_file_path = os.path.join(download_dir, document.file_name)
    # Faylni yuklab olish
    response = requests.get(file_url)
    with open(local_file_path, 'wb') as f:
        f.write(response.content)

    return local_file_path