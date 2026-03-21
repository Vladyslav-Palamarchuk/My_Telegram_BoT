import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

from keyboards import get_shop_keyboard # імпортуєм наші модельки клави


from aiogram.fsm.state import StatesGroup, State
       #fsm- механізм який покроково запамятовує на чому зупигився коистувач
from aiogram.fsm.context import FSMContext
       #керування кроками та збереження даних користувача

from db import init_db, add_lead


#завантажую токен з файлу .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

#запускаємо бота та диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


class From(StatesGroup):
    waiting_for_phone = State()


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
async def call_manager(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Заявка прийнята")
    await callback.message.answer("Будь ласка введіть ваш номер телефону.")
    await state.set_state(From.waiting_for_phone)


@dp.message(From.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await message.answer(f"Дякуємо, {message.from_user.first_name}!"
                         f"Номер {phone} збережено. Менеджер зателефонує.")


    add_lead(message.from_user.full_name, message.from_user.id, phone)
    await message.answer("Дякуємо, ваша заявка збережена в базі даних.")
    await state.clear()




# головна перевірка
async def main():
    init_db() #наша таблиця створюється при запуску
    print("--бот активний--")
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

