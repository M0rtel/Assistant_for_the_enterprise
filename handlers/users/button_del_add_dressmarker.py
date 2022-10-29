import csv
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup

from loader import dp
from states.order import DelAddDress
from keyboards.default.keyboard_menu import kb_menu


@dp.message_handler(Text(equals=['Добавить швею в список']))
async def buttons_data_time_hands(message: types.Message):
    print('Добавить швею в список')
    await message.answer('Введите фамилию новой швеи!')
    await DelAddDress.DelAdd1.set()


@dp.message_handler(state=DelAddDress.DelAdd1)
async def DelAdd1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(delAdd1=answer)
    data = await state.get_data()
    text_blank = data.get('delAdd1')
    if text_blank == 'Назад':
        await state.finish()
        await message.answer('Назад', reply_markup=kb_menu)

    else:
        print(text_blank)
        with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv',
                  'a',  newline='', encoding='utf-8') as f_object:
            f_object.write(text_blank + '\n')
            f_object.close()

        await state.finish()
        await message.answer(f'Фамилия новой швеи: {text_blank}', reply_markup=kb_menu)


@dp.message_handler(Text(equals=['Удалить швею из списка']))
async def buttons_data_time_hands(message: types.Message):
    print('Удалить швею из списка')
    if not os.path.exists('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv'):
        await message.answer('У вас нет швей!', reply_markup=kb_menu)

    else:
        kb_dressmaker_dismiss = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv',
                  'r', newline='', encoding='utf-8') as File:
            reader = csv.reader(File)
            for row in reader:
                kb_dressmaker_dismiss.add(types.KeyboardButton(text=f'{row[0]}'))

        kb_dressmaker_dismiss.add(types.KeyboardButton(text='Назад'))
        await message.answer('Удалить швею из списка', reply_markup=kb_dressmaker_dismiss)
        await DelAddDress.DelAdd2.set()


@dp.message_handler(state=DelAddDress.DelAdd2)
async def DelAdd2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(delAdd2=answer)
    data = await state.get_data()
    text_blank = data.get('delAdd2')

    list_in_order = []
    with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv',
              'r', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            list_in_order.append(row[0])

    if text_blank == 'Назад':
        await state.finish()
        await message.answer('Назад', reply_markup=kb_menu)

    elif text_blank in list_in_order:
        list_in_order.remove(text_blank)

        if os.path.exists('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv'):
            os.remove('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv')

        for last_name in list_in_order:
            with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv',
                      'a',  newline='', encoding='utf-8') as f_object:
                f_object.write(last_name + '\n')

        await state.finish()
        await message.answer(f'Вы удалили швею: {text_blank}', reply_markup=kb_menu)

    else:
        await message.answer('Такой фамилии не существует!')
