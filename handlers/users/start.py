from aiogram import types
from loader import dp

from keyboards.default import kb_menu


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer("Здравствуйте, выберите кем вы работаете в компании!", reply_markup=kb_menu)
