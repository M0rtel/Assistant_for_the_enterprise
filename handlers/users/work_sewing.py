import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default import kb_menu, kb_del_save_message, kb_status_sewing
from states.order import Sewing


from loader import dp


# @dp.message_handler(Text(equals=['Шитьё']))
# async def sewing(message: types.Message):
#     print('ЗАКАЗЫ')
#     kb_mane_sewing = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#
#     with open('C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Заказы.csv',
#               'r', newline='', encoding='utf-8') as File:
#         reader = csv.reader(File)
#         for row in reader:
#             kb_mane_sewing.add(types.KeyboardButton(text=f'{row[0]}'))
#
#     kb_mane_sewing.add(types.KeyboardButton(text='Назад'))
#     await message.answer("Выберите заказ", reply_markup=kb_mane_sewing)


@dp.message_handler(Text(equals=['Шитьё']))
async def blanks(message: types.Message):
    print('Шитьё')
    await message.answer('В формате сообщения вводите информация о времени, затраченное на работу')
    await Sewing.sewing1.set()


@dp.message_handler(state=Sewing.sewing1)
async def sewing1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sewing1=answer)
    data = await state.get_data()
    text_sewing = data.get('sewing1')

    if text_sewing == 'Назад':
        await state.finish()
        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")

        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await state.finish()
        await message.answer(f'Текст про потраченное время на заготовки:\n'
                             f'{text_sewing}')
        with open(
                f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt',
                'w', encoding='utf-8') as file:
            file.write(text_sewing)

        await message.answer('Вас устраивает набранное вами сообщение?', reply_markup=kb_del_save_message)
        await Sewing.sewing2.set()


@dp.message_handler(state=Sewing.sewing2)
async def sewing2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sewing2=answer)
    data = await state.get_data()
    text_del_add = data.get('sewing2')

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
        await Sewing.sewing1.set()

    elif text_del_add == 'Сохранить':
        text = open(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank_lol{message.from_user.id}.txt",
            'r', encoding='utf-8').read()

        with open(
                f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
                'a', encoding='utf-8') as file:
            file.write(f" {text}")

        await state.finish()
        await message.answer('Данные сохранены!')
        await message.answer('Теперь выберите статус заказа', reply_markup=kb_status_sewing)
