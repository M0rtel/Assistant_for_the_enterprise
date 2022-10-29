from aiogram import types
from aiogram.dispatcher.filters import Text

from states.order import Blanks

from loader import dp

from keyboards.default.keyboard_menu import kb_menu


@dp.message_handler(Text(equals=['Удалить']))
async def del_message(message: types.Message):
    print('Удалить')
    await message.answer('Текст про заготовку был удалён!!\n'
                         'Введите новый текст!')
    await Blanks.blank1.set()


@dp.message_handler(Text(equals=['Сохранить']))
async def save_message(message: types.Message):
    with open(f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
              'r', encoding='utf-8') as file:
        text_blank = file.read()

    print(text_blank)
    await message.answer('Текст сохранён!!', reply_markup=kb_menu)

