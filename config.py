import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import  ParseMode
from aiogram.client.default import DefaultBotProperties
from funksiya import bot_ishga_tushganda , bot_ishdan_toxtanda,start_bosganda,wikipedia
from aiogram.filters import CommandStart

dp = Dispatcher()
TOKEN = "8385216008:AAEfx5fluKVX1dk4Qye1A9CsoDF_H-8PZL4"
async def main():
    dp.startup.register(bot_ishga_tushganda)
    dp.message.register(start_bosganda, CommandStart())
    dp.message.register(wikipedia)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(bot_ishdan_toxtanda)
    await dp.start_polling(bot)

asyncio.run(main())