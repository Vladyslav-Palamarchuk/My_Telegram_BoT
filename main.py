import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv


#завантажую токен з файлу .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

#запускаємо бота та диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


#обробляємо команду старт
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.full_name}! Я бот і ти мене створив.")


# головна перевірка
async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

