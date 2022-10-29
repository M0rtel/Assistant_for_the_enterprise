from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_data_time = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В ручную'),
            KeyboardButton(text='Автоматически')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
