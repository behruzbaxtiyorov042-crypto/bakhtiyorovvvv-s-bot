from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from imtixon3 import MyInfo


async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(text='Bot ishga tushdi', chat_id=7874452621)

async def bot_toxtaganda(bot: Bot):
    await bot.send_message(text='Bot toxtadi', chat_id=7874452621)


async def start_bosganda(message: Message, state: FSMContext):
    await message.answer('Assalomu alaykum!\n \n Oyin rejasini tuzamiz. \n \n 1. Bugungi sana?')
    await state.set_state(MyInfo.Bugungi_sana)

async def Bugungi_sana(message: Message, state: FSMContext):
    await state.update_data(bugungi_sana=message.text)
    await message.answer('2. Oyin boshlash vaqti?')
    await state.set_state(MyInfo.Oyin_Boshlash_Vaqti)

async def Oyin_Boshlash_Vaqti(message: Message, state: FSMContext):
    await state.update_data(OyinBoshlashVaqti=message.text)
    await message.answer('3. O‘yin turi qanday?')
    await state.set_state(MyInfo.Oyin_Turi)

async def Oyin_Turi(message: Message, state: FSMContext):
    await state.update_data(oyingTuri=message.text)
    await message.answer('4. O‘yin joyi qayerda?')
    await state.set_state(MyInfo.Oyin_joyi)

async def Oyin_joyi(message: Message, state: FSMContext):
    await state.update_data(Oyin_joyi=message.text)
    await message.answer('5. Ishtirokchilar soni nechta')
    await state.set_state(MyInfo.Ishtrokchilar_soni)

async def Ishtrokchilar_soni(message: Message, state: FSMContext):
    await state.update_data(Ishtrokchilar_soni=message.text)
    await message.answer('6. Jamoa nomi nima')
    await state.set_state(MyInfo.Jamoa_nomi)

async def Jamoa_nomi(message: Message, state: FSMContext):
    await state.update_data(Jamoa_nomi=message.text)
    await message.answer('7. Kirish bepulmi')
    await state.set_state(MyInfo.Kirish_bepulmi)

async def Kirish_bepulmi(message: Message, state: FSMContext):
    await state.update_data(Kirish_bepulmi=message.text)
    await message.answer('8. O‘yindan keyin atirfand bo‘ladimi')
    await state.set_state(MyInfo.Oyindan_keyyin_atirfand)

async def Oyindan_keyyin_atirfand(message: Message, state: FSMContext):
    await state.update_data(Oyindan_keyyin_atirfand=message.text)
    await message.answer('9. O‘yinda musiqa bo‘ladimi')
    await state.set_state(MyInfo.Oyinda_musiqa_buladimi)

async def Oyinda_musiqa_buladimi(message: Message, state: FSMContext):
    await state.update_data(Oyinda_musiqa_buladimi=message.text)
    await message.answer('10. Qo‘shimcha izohlar bormi')
    await state.set_state(MyInfo.Qoshimcha_izoh)

async def Qoshimcha_izoh(message: Message, state: FSMContext):
    await state.update_data(Qoshimcha_izoh=message.text)
    data = await state.get_data()

    matn = f""" MA'LUMOTLARINGIZ:
Bugungi sana: {data['bugungi_sana']}
O'yin boshlanish vaqti: {data['OyinBoshlashVaqti']}
O'yin turi: {data['oyingTuri']}
O'yin joyi: {data['Oyin_joyi']}
Ishtirokchilar soni: {data['Ishtrokchilar_soni']}
Jamoa nomi: {data['Jamoa_nomi']}
Kirish bepulmi ?: {data['Kirish_bepulmi']}
O'yindan keyin atirfand: {data['Oyindan_keyyin_atirfand']}
O'yinda musiqa bo‘ladimi ?: {data['Oyinda_musiqa_buladimi']}
Qo'shimcha izoh: {data['Qoshimcha_izoh']}
"""
    await message.answer(matn)
    await state.clear()