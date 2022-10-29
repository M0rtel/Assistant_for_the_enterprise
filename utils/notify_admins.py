import logging

from aiogram import Dispatcher

from data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            text = 'Бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as ex:
            logging.exception(ex)
            