from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default import kb_del_save_message, kb_menu
from states.order import Blanks

from loader import dp


@dp.message_handler(Text(equals=['Заготовки']))
async def blanks(message: types.Message):
    print('Заготовки')
    await message.answer('В формате сообщения вводите информация о времени, затраченное на работу')
    await Blanks.blank1.set()


@dp.message_handler(state=Blanks.blank1)
async def order1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(blank1=answer)
    data = await state.get_data()
    text_blank = data.get('blank1')
    if text_blank == 'Назад':
        await state.finish()
        await message.answer('Назад', reply_markup=kb_menu)

    else:
        await message.answer(f'Текст про потраченное время на заготовки:\n'
                             f'{text_blank}')
        with open(f'C:\D\Program\Программирование\Проекты\Python\Проект_Юры\data\Сохранённые состояния\save_text_blank{message.from_user.id}.txt',
                  'w', encoding='utf-8') as file:
            file.write(text_blank)

        await state.finish()
        await message.answer('Вас устраивает набранное вами сообщение?', reply_markup=kb_del_save_message)
