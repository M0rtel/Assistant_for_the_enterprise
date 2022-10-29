from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_dressmaker_def_add = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить швею в список'),
            KeyboardButton(text='Удалить швею из списка')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
