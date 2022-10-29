from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Директор')
        ],
        # [
        #     KeyboardButton(text='Николай Иванович')
        # ],
        [
            KeyboardButton(text='Швея')
        ]
    ],
    resize_keyboard=True
)
