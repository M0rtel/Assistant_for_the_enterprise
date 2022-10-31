from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import os

from keyboards.default import kb_name_work, kb_menu

from loader import dp
from states.order import DataTimeHand


@dp.message_handler(Text(equals=['В ручную']))
async def buttons_data_time_hands(message: types.Message):
    await message.answer("Вы выбрали вписать дату и временя в ручную.\n"
                         "Пример: 13.05.2015 16:53", reply_markup=kb_name_work)
    await DataTimeHand.datatime1.set()


@dp.message_handler(state=DataTimeHand.datatime1)
async def datatime1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(datatime1=answer)
    data = await state.get_data()
    data_time = data.get('datatime1')
    if data_time.count('.') == 2 and data_time.count(':') == 1 and data_time.count(' ') == 1:
        await state.finish()
        with open(f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
                  'a', encoding='utf-8') as file:
            file.write(f" {data_time}")
        await message.answer(f'Написанная дата и время: {data_time}')

    elif data_time == 'Назад':
        await state.finish()
        if os.path.exists(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt"):
            os.remove(f"C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt")
        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await message.answer('Неверно введённая дата и время')


@dp.message_handler(Text(equals=['Автоматически']))
async def buttons_data_time_automatically(message: types.Message):
    data_time_auto = message.date.strftime('%d-%m-%Y %H:%M').replace('-', '.')
    print(data_time_auto)
    with open(
            f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
            'a', encoding='utf-8') as file:
        file.write(f" {data_time_auto}")
    await message.answer(f"Вы выбрали автоматическое вписывание даты и времени "
                         f"{data_time_auto}", reply_markup=kb_name_work)
