"""
import asyncio
from aiogram import Bot, Dispatcher, types, F

# --- НАСТРОЙКИ ---
API_TOKEN = '8248530120:AAFMcGxFs3UMP014Y6iiWzyXzE--_-mvadM'
# Твой личный ID (чтобы бот присылал фото тебе в личку) 
# или ID чата, где сидит другой бот
TARGET_CHAT_ID = 6479786059 

ALLOWED_SOURCES = {
    -1003412963252: 162,  # ID группы : ID топика
}

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.photo)
async def handle_photos(message: types.Message):
    chat_id = message.chat.id
    thread_id = message.message_thread_id

    if chat_id in ALLOWED_SOURCES and thread_id == ALLOWED_SOURCES[chat_id]:
        # Название супергруппы для подписи
        caption_text = f"Из группы: {message.chat.title}"
        
        # Отправляем фото в целевой чат
        await bot.send_photo(
            chat_id=TARGET_CHAT_ID,
            photo=message.photo[-1].file_id,
            caption=caption_text
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  """



import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiohttp import web

# --- НАСТРОЙКИ ---
API_TOKEN = '8248530120:AAFMcGxFs3UMP014Y6iiWzyXzE--_-mvadM'

# Твой личный ID (узнай его у @userinfobot)
#MY_PERSONAL_ID = 783634711
RECIPIENTS = [783634711, 8570806119] 
# Список групп и топиков
# { ID_группы: ID_топика }
ALLOWED_SOURCES = {
    -1003412963252: 162,  # Первая группа
}

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция-заглушка для Render (чтобы бот не засыпал)
async def handle_health(request):
    return web.Response(text="Бот работает!")
@dp.message(F.photo)
async def handle_photos(message: types.Message):
    chat_id = message.chat.id
    thread_id = message.message_thread_id

    if chat_id in ALLOWED_SOURCES and thread_id == ALLOWED_SOURCES[chat_id]:
        group_name = message.chat.title
        photo_id = message.photo[-1].file_id
        caption_text = f"Новое фото из группы: {group_name}"
        
        # Цикл для рассылки всем получателям
        for user_id in RECIPIENTS:
            try:
                await bot.send_photo(
                    chat_id=user_id,
                    photo=photo_id,
                    caption=caption_text
                )
            except Exception as e:
                # Если кто-то не запустил бота, выведется ошибка только для него
                print(f"Не удалось отправить пользователю {user_id}: {e}")
                


"""@dp.message(F.photo)
async def handle_photos(message: types.Message):
    chat_id = message.chat.id
    thread_id = message.message_thread_id

    # Проверяем, пришло ли фото из нужной группы и нужного топика
    if chat_id in ALLOWED_SOURCES and thread_id == ALLOWED_SOURCES[chat_id]:
        # Название группы для подписи
        group_name = message.chat.title
        
        # Отправляем фото тебе в личку
        try:
            await bot.send_photo(
                chat_id=MY_PERSONAL_ID,
                photo=message.photo[-1].file_id,
                caption=f"{group_name}"
            )
        except Exception as e:
            print(f"Ошибка отправки: {e}. Возможно, вы не написали /start боту в личку.")
        try:
            await bot.send_photo(
                chat_id=MY_PERSONAL_ID1,
                photo=message.photo[-1].file_id,
                caption=f"{group_name}"
            )
        except Exception as e:
            print(f"Ошибка отправки: {e}. Возможно, вы не написали /start боту в личку.")"""

async def main():
    # Настройка веб-сервера для Render (порт 8080)
    app = web.Application()
    app.router.add_get("/", handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    asyncio.create_task(site.start())

    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
