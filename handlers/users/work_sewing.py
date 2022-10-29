import csv

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup


from loader import dp


@dp.message_handler(Text(equals=['Шитьё']))
async def sewing(message: types.Message):
    print('ЗАКАЗЫ')
    kb_mane_sewing = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv',
              'r', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            kb_mane_sewing.add(types.KeyboardButton(text=f'{row[0]}'))

    kb_mane_sewing.add(types.KeyboardButton(text='Назад'))
    await message.answer("Выберите заказ", reply_markup=kb_mane_sewing)

