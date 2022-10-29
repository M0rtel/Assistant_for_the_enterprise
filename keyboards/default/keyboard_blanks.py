from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_blanks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выбрать заказ')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
