import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart
from imtixon2 import (start_bosganda, bot_toxtaganda, bot_ishga_tushganda,Bugungi_sana, Oyin_Boshlash_Vaqti, Oyin_Turi,Oyin_joyi, Ishtrokchilar_soni, Jamoa_nomi,Kirish_bepulmi, Oyindan_keyyin_atirfand,Oyinda_musiqa_buladimi, Qoshimcha_izoh)
from imtixon3 import MyInfo

TOKEN = "8385216008:AAEfx5fluKVX1dk4Qye1A9CsoDF_H-8PZL4"

dp = Dispatcher()

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.startup.register(bot_ishga_tushganda)
    dp.shutdown.register(bot_toxtaganda)

    dp.message.register(start_bosganda, CommandStart())
    dp.message.register(Bugungi_sana, MyInfo.Bugungi_sana)
    dp.message.register(Oyin_Boshlash_Vaqti, MyInfo.Oyin_Boshlash_Vaqti)
    dp.message.register(Oyin_Turi, MyInfo.Oyin_Turi)
    dp.message.register(Oyin_joyi, MyInfo.Oyin_joyi)
    dp.message.register(Ishtrokchilar_soni, MyInfo.Ishtrokchilar_soni)
    dp.message.register(Jamoa_nomi, MyInfo.Jamoa_nomi)
    dp.message.register(Kirish_bepulmi, MyInfo.Kirish_bepulmi)
    dp.message.register(Oyindan_keyyin_atirfand, MyInfo.Oyindan_keyyin_atirfand)
    dp.message.register(Oyinda_musiqa_buladimi, MyInfo.Oyinda_musiqa_buladimi)
    dp.message.register(Qoshimcha_izoh, MyInfo.Qoshimcha_izoh)

    await dp.start_polling(bot)

asyncio.run(main())