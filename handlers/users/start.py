import os

from aiogram import types
from loader import dp

from keyboards.default import kb_menu


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
        os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

    if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt"):
        os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt")

    await message.answer("Здравствуйте, выберите кем вы работаете в компании!", reply_markup=kb_menu)
