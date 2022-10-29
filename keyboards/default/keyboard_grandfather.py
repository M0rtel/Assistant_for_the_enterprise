from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_grandfather = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Нужно сделать'),
            KeyboardButton(text='Сделанное')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
