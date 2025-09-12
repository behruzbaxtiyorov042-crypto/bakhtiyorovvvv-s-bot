from aiogram.types import Message
from aiogram import Bot

async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(chat_id=7874452621, text='Bot ishga tushdi...')

async def bot_ishdan_toxtanda(bot: Bot):
    await bot.send_message(chat_id=7874452621, text='Bot ishdan to‘xtadi...')

async def start_bosganda(message: Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.first_name}!")

async def wikipedia(message: Message):
    try:
        import wikipedia
        wikipedia.set_lang('uz')
        natija = wikipedia.summary(message.text, sentences=5)
        await message.answer(natija, reply_to_message_id=message.message_id)
    except:
        await message.answer("Bunday ma'lumot bazada mavjud emas.")