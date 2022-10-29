import csv
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from loader import dp

from states.order import Orders
from keyboards.default import kb_dressmaker_def_add, kb_menu


@dp.message_handler(text='Добавить заказ')
async def order_add(message: types.Message):
    print('Добавить заказ')
    await message.answer('Введите названия заказа и его номер\n'
                         'Пример: №15124 Арма 10м')
    await Orders.order1.set()


@dp.message_handler(state=Orders.order1)
async def order1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(order1=answer)
    data = await state.get_data()
    number_name = data.get('order1')
    if number_name.count('№') == 1 and number_name.count(' ') >= 1:
        with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv',
                  'a',  newline='', encoding='utf-8') as f_object:
            f_object.write(number_name + '\n')
            f_object.close()

        await state.finish()
        await message.answer(f'Добавлен новый заказ: {number_name}', reply_markup=kb_menu)

    elif number_name == 'Назад':
        await state.finish()
        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await message.answer('Неверно введены данные о новом заказе')


@dp.message_handler(text='Удалить заказ')
async def order_del(message: types.Message):
    print('Удалить заказ заказа')
    if not os.path.exists('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv'):
        await message.answer('У вас нет заказов!', reply_markup=kb_menu)

    else:
        kb_dressmaker_del = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv',
                  'r', newline='', encoding='utf-8') as File:
            reader = csv.reader(File)
            for row in reader:
                kb_dressmaker_del.add(types.KeyboardButton(text=f'{row[0]}'))

        kb_dressmaker_del.add(types.KeyboardButton(text='Назад'))

        await message.answer('Выберите заказ, который нужно удалить', reply_markup=kb_dressmaker_del)
        await Orders.order3.set()


@dp.message_handler(state=Orders.order3)
async def order3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(order3=answer)
    data = await state.get_data()
    name_order = data.get('order3')

    list_in_order = []
    with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv',
              'r', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            list_in_order.append(row[0])

    if name_order == 'Назад':
        await state.finish()
        await message.answer('Назад', reply_markup=kb_menu)

    elif name_order in list_in_order:
        list_in_order.remove(name_order)

        if os.path.exists('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv'):
            os.remove('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv')

        for last_name in list_in_order:
            with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv',
                      'a', newline='', encoding='utf-8') as f_object:
                f_object.write(last_name + '\n')

        await state.finish()
        await message.answer(f'Вы удалили заказ: {name_order}', reply_markup=kb_menu)

    else:
        await message.answer('Такого заказа не существует!')


@dp.message_handler(text='Швеи')
async def dressmaker_def_add(message: types.Message):
    print('Швеи')
    await message.answer('Выберите команду!', reply_markup=kb_dressmaker_def_add)
