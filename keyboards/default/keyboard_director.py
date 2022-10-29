from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_director = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Добавить заказ'),
            KeyboardButton(text='Удалить заказ'),
            KeyboardButton(text='Швеи')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
