from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_sewing = ReplyKeyboardMarkup(
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
