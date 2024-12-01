import requests
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from asyncio import create_task

# Importlar
from loader import dp
from utils import buttons, texts
from services.services import get_lesson_by_id
from utils.env import BOT_TOKEN



async def lesson_send_task(message: Message, state: FSMContext):
    """
    Asosiy video darslikni API orqali yuboradigan funksiya
    """
    # Lesson ID olish
    lesson_id = int(message.text.split('-')[0])
    await state.update_data({'lesson_id': lesson_id})

    # Lessonni bazadan olish
    lesson = get_lesson_by_id(lesson_id)

    if lesson:
        # Video, rasm va fayllarni guruhlash
        media_group = []
        for video in lesson['videos']:
            media_group.append({
                'type': 'video',
                'media': video['vide_id'],
                'caption': f"Video {video['id']}" if video.get('id') else None
            })

        photo_group = []
        for photo in lesson['photos']:
            photo_group.append({
                'type': 'photo',
                'media': photo['photo_id'],
                'caption': f"Photo {photo['id']}" if photo.get('id') else None
            })

        # Fayllarni alohida yuborish
        for file in lesson['files']:
            payload = {
                'chat_id': message.chat.id,
                'document': file['file_id'],
                'caption': f"File {file['id']}" if file.get('id') else None,
                'protect_content': True
            }
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
            requests.post(url, json=payload)

        # Ovozli xabarlarni yuborish
        for voice in lesson['voices']:
            payload = {
                'chat_id': message.chat.id,
                'voice': voice['voice_id'],
                'caption': f"Voice {voice['id']}" if voice.get('id') else None,
                'protect_content': True
            }
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendVoice'
            requests.post(url, json=payload)

        # Video va rasm guruhlarini yuborish
        for group in [media_group, photo_group]:
            if group:
                payload = {
                    'chat_id': message.chat.id,
                    'media': group[:10],  # Telegramda har bir media-guruh maksimal 10 element
                    'protect_content': True
                }
                url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMediaGroup'
                requests.post(url, json=payload)

        # Asosiy dars ma'lumotlarini yuborish
        title = lesson['title']
        description = lesson['description']
        date = lesson['date']

        caption_text = texts.lessons(
            title=title,
            description=description,
            date=date,
        )

        # Topshiriq statusiga qarab tugmalarni yuborish
        if not lesson['is_lesson_homework_status'] == 'topshirilmagan':
            await message.answer(
                text=caption_text,
                reply_markup=buttons.HOME_WORKS
            )
        else:
            await message.answer(
                text=caption_text,
                reply_markup=buttons.HOME_WORKS_DOWNLOAD
            )
    else:
        # Agar lesson topilmasa
        await message.answer(texts.NOT_COURSE)


@dp.message_handler(lambda message: message.text.endswith('-dars'), state='*')
async def lesson_send(message: Message, state: FSMContext):
    await create_task(lesson_send_task(message, state))
