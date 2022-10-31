import os
import csv

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(Text(equals=['Готово', 'Не готов']))
async def ready_and_not_ready(message: types.Message):
    with open(
            f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
            'r', encoding='utf-8') as f:
        data = f.read().split(' ')

    data_and_name = []
    data_and_name.append(
        {
            'Швея': data[0],
            'Дата': data[1],
            'Время': data[2],
            'Раздел работы': 'Шитьё',
            'Текст': data[3],
            'Статус': message.text
        }
    )

    # with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Данные_по_заказам.csv',
    #           'w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(
    #         (
    #             'Швея',
    #             'Дата',
    #             'Время',
    #             'Раздел работы',
    #             'Текст',
    #             'Статус'
    #         )
    #     )

    for x in data_and_name:
        with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Данные_по_заказам.csv',
                  'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    x['Швея'],
                    x['Дата'],
                    x['Время'],
                    x['Раздел работы'],
                    x['Текст'],
                    x['Статус']
                )
            )

    if os.path.exists(
            f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
        os.remove(
            f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

    if os.path.exists(
            f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt"):
        os.remove(
            f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt")

    await message.answer('Данные добавлены', reply_markup=kb_menu)
