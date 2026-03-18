import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

from keyboards import get_shop_keyboard # імпортуєм наші модельки клави



#завантажую токен з файлу .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

#запускаємо бота та диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


#обробляємо команду старт
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.full_name}!"
                         f"Оберіть товар у нашому магазині: ",
                         reply_markup=get_shop_keyboard())
                         #reply_markup -прикріплює до рядка кнопки які мтворили


@dp.callback_query(F.data == "купити курс Python") #F.data- перевірка
async def process_buy_python(callback: types.CallbackQuery): #types.CallbackQuery-параметри кнопки(різі)
    await callback.answer("Чудовий вибір!")
    await callback.message.answer("Ви обрали курс Python, "
                                  "вартість 1000грн., надіслати реквізити?")


@dp.callback_query(F.data == "купити aiogram бібліотеку")
async def process_buy_aiogram(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Ви обрали гайд по ботам, вартість 600грн.")


@dp.callback_query(F.data == "Зв'язатися з менеджером")
async def call_manager(callback: types.CallbackQuery):
    await callback.answer("Заявка прийнята")
    await callback.message.answer("Менеджер вам телефонує.")



# головна перевірка
async def main():
    print("--бот активний--")
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

