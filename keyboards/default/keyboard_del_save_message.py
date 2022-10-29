from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_del_save_message = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сохранить'),
            KeyboardButton(text='Удалить')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
