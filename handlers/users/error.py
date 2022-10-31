from aiogram import types

from keyboards.default import kb_menu
from loader import dp


@dp.message_handler(content_types=["text"])
async def echo(message: types.Message):
    await message.answer('Неверная команда')

