import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from gb_bot.settings import config


class GBBot:
    def __init__(self):
        self.bot = Bot(token=config.TOKEN)

    async def start(self, message: Message, dialog_manager: DialogManager):
        from gb_bot.states import DefaultStates
        await dialog_manager.start(DefaultStates.main, mode=StartMode.RESET_STACK)

    async def main(self):
        from gb_bot.setup import setup_default_dialogs
        logging.basicConfig(level=logging.INFO)
        dialog = setup_default_dialogs()
        dp = Dispatcher()
        dp.message.register(self.start, CommandStart())
        dp.include_router(dialog)
        setup_dialogs(dp)

        await dp.start_polling(self.bot)


_gb_bot = GBBot()