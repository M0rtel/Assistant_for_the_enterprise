import csv
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from loader import dp

from keyboards.default import kb_grandfather, kb_data_time
from keyboards.default import kb_menu
from keyboards.default import kb_director

from data.config import ADMINS_ID
from states.order import LastName


@dp.message_handler(text='Директор')
async def buttons_director(message: types.Message):
    if message.from_user.id in ADMINS_ID:
        print('Директор')
        await message.answer('Здравствуйте, Дмитрий Александрович!', reply_markup=kb_director)

    else:
        await message.answer('У вас недостаточно прав, чтобы использовать данную команду!')


# @dp.message_handler(text='Николай Иванович')
# async def buttons_grandfather(message: types.Message):
#     print('Дедушка')
#     await message.answer('Здравствуйте, Николай Иванович!', reply_markup=kb_grandfather)


@dp.message_handler(text='Швея')
async def buttons_dressmaker(message: types.Message):
    print('Швея')

    kb_dressmaker_name = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv',
              'r', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            kb_dressmaker_name.add(types.KeyboardButton(text=f'{row[0]}'))

    kb_dressmaker_name.add(types.KeyboardButton(text='Назад'))

    await message.answer("Выберите вашу фамилию?", reply_markup=kb_dressmaker_name)
    await LastName.lastname1.set()


@dp.message_handler(state=LastName.lastname1)
async def order3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(lastname1=answer)
    data = await state.get_data()
    lastname = data.get('lastname1')

    list_in_order = []
    with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Список_фамилий.csv',
              'r', newline='', encoding='utf-8') as File:
        reader = csv.reader(File)
        for row in reader:
            list_in_order.append(row[0])

    if lastname in list_in_order:
        await state.finish()
        with open(f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
                  'w', encoding='utf-8') as file:
            file.write(lastname)
        await message.answer(f"Здравствуйте, {lastname}! "
                             "Вы хотите вручную написать дату и время или сделать это автоматически?",
                             reply_markup=kb_data_time)

    elif lastname == 'Назад':
        await state.finish()
        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")
        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await message.answer(f"Неверная команда: {lastname}")


@dp.message_handler(text='Назад')
async def buttons_back(message: types.Message):
    if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
        os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

    if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt"):
        os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt")

    await message.answer("Назад", reply_markup=kb_menu)
