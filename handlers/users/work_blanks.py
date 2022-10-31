from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import os
import csv

from keyboards.default import kb_del_save_message, kb_menu
from states.order import Blanks

from loader import dp


@dp.message_handler(Text(equals=['Заготовки']))
async def blanks(message: types.Message):
    print('Заготовки')
    await message.answer('В формате сообщения вводите информация о времени, затраченное на работу')
    await Blanks.blank1.set()


@dp.message_handler(state=Blanks.blank1)
async def blank1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(blank1=answer)
    data = await state.get_data()
    text_blank = data.get('blank1')

    if text_blank == 'Назад':
        await state.finish()
        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await state.finish()
        await message.answer(f'Текст про потраченное время на заготовки:\n'
                             f'{text_blank}')
        with open(
                f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt',
                'w', encoding='utf-8') as file:
            file.write(text_blank)

        await message.answer('Вас устраивает набранное вами сообщение?', reply_markup=kb_del_save_message)
        await Blanks.blank2.set()


@dp.message_handler(state=Blanks.blank2)
async def blank2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(blank2=answer)
    data = await state.get_data()
    text_del_add = data.get('blank2')

    if text_del_add == 'Назад':
        await state.finish()
        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt")

        await message.answer('Назад', reply_markup=kb_menu)

    elif text_del_add == 'Удалить':
        await state.finish()
        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt")
        await message.answer('В формате сообщения вводите информация о времени, затраченное на работу')
        await Blanks.blank1.set()

    elif text_del_add == 'Сохранить':
        text = open(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt",
            'r', encoding='utf-8').read()

        with open(
                f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
                'a', encoding='utf-8') as file:
            file.write(f" {text}")

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
                'Раздел работы': 'Заготовка',
                'Текст': data[3],
                'Статус': 'Готов'
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

        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt")

        await state.finish()
        await message.answer('Данные сохранены!', reply_markup=kb_menu)
