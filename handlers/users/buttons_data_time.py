from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

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
        await message.answer(f'Написанная дата и время: {data_time}')
        await state.finish()

    elif data_time == 'Назад':
        await state.finish()
        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await message.answer('Неверно введённая дата и время')


@dp.message_handler(Text(equals=['Автоматически']))
async def buttons_data_time_automatically(message: types.Message):
    print(message.date.strftime('%d-%m-%Y %H:%M').replace('-', '.'))

    await message.answer(f"Вы выбрали автоматическое вписывание даты и времени "
                         f"{message.date.strftime('%d-%m-%Y %H:%M').replace('-', '.')}", reply_markup=kb_name_work)
