from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_name_work = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Шитьё'),
            KeyboardButton(text='Заготовки')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
