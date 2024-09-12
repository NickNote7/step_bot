import asyncio
import logging

from aiogram import Dispatcher, Bot
from config_data.config import load_config

async def start() -> None:
    config = load_config()
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')

    BOT = Bot(token=config.tg_bot.token)
    BOT_DISPATCHER = Dispatcher()

    await BOT.delete_webhook(drop_pending_updates=True)
    await BOT_DISPATCHER.start_polling(BOT)

if __name__ == "__main__":
    asyncio.run(start())

