from aiogram.fsm.state import State, StatesGroup

class MyInfo(StatesGroup):
    Bugungi_sana = State()
    Oyin_Boshlash_Vaqti = State()
    Oyin_Turi = State()
    Oyin_joyi = State()
    Ishtrokchilar_soni = State()
    Jamoa_nomi = State()
    Kirish_bepulmi = State()
    Oyindan_keyyin_atirfand = State()
    Oyinda_musiqa_buladimi = State()
    Qoshimcha_izoh = State()