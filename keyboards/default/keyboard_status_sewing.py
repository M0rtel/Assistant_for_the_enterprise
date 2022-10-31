from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_status_sewing = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Готов'),
            KeyboardButton(text='Не готов')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
