from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
# імпорти для створення кнопок їх структуру та саму кнопку в боті

def get_shop_keyboard():
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text="Курс Python", callback_data="купити курс Python"))
    builder.row(InlineKeyboardButton(text="Гайд по ботам", callback_data="купити aiogram бібліотеку"))
    builder.row(InlineKeyboardButton(text="Консультація.",callback_data="Зв'язатися з менеджером"))
    return builder.as_markup() # ця функція повертає створену вище клаву
                               # callback_data - клавіша, як команда для бота




