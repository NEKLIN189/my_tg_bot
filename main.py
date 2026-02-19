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
  
