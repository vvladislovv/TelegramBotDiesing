from aiogram import Bot, Dispatcher,executor, types
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup
from Button import kb_btns,kb_linkBtns,buyMain,Btny
import time

StorageMemary = MemoryStorage()
BotAPI = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=BotAPI,storage=StorageMemary)

class QuestStorge(StatesGroup):
    def QuestGroup():
        OneQuset = State()
        TwoQuset = State()
        ThreeQuset = State()
        FourQuset = State()
        FiveQuset = State()
        
    def QuestCompany():
        OneQuset = State()
        TwoQuset = State()
        ThreeQuset = State()
        FourQuset = State()
        FiveQuset = State()

@dp.message_handler(commands=['start', 's'])
async def NewUserOpenKB(message: types.Message) -> None:
    TextTable = [ 
        'Привет! Я бот Митя Кондрачук',
        '',
        'У тебя внизу появились кнопки, нажми на одну из них, чтобы продолжить общение со мной!'
    ]
    await message.answer(text='\n'.join(TextTable),reply_markup=kb_btns)
'''
@dp.message_handler(content_types=['text'])
async def ContextCheck(msg: types.Message):
    if msg.text == 'Ознакомиться с портфолио':
        TextTable = [
        'Навигация по моему портфолио 📌',
        'Переходи ниже по кнопке'
        ]
        await msg.answer(text='\n'.join(TextTable),reply_markup=kb_linkBtns)
    elif msg.text == 'Прайс услуг':
        TextTable = [
        'Визитка — 2.500 рублей',
        'Сертификат — 3.000 рублей',
        'Пост — 2.000 рублей',
        'Афиша — 3.000 рублей',
        '',
        'Оформление группы VK — от 5.000 рублей',
        'Оформление YouTube канала — от 5.000 рублей',
        'Оформление презентации — от 5.000 рублей',
        'Логотип — от 10.000 рублей',
        '',
        'Логобук — Цена обсуждается лично',
        'Брендбук — Цена обсуждается лично',
        'Разработка фирменного стиля — Цена обсуждается лично',
        '',
        'Если услуги нет в списке - нажмите на кнопку Услуги нет',
        ]
        await msg.answer(text='\n'.join(TextTable), reply_markup=buyMain)
    elif msg.text == 'Сделать заказ':
        await msg.answer(f'Сейчас мне надо задать тебе пару вопросов')
        time.sleep(0.5)
        await msg.answer('Вы являетесь компанией или частным лицом?',reply_markup=Btny)
'''

    #await message.answer('',reply_markup=types.ReplyKeyboardRemove())

    #await message.answer('',reply_markup=types.ReplyKeyboardRemove())
'''
@dp.callback_query_handler()
async def vote_callBack(callBack: types.CallbackQuery):
    if callBack.data == 'Услуги':
       await callBack.message.answer(text="Вашей услуги нет в списке? Напишите мне лично, и мы обсудим то, что вам нужно @kondrachuk_me")
   
'''    


@dp.message_handler(text = 'Компанией')
async def ButtonQuest(msg: types.Message):
    if msg.text == 'Компанией':
        await msg.answer('Какое название у вашей компании?')
        await QuestStorge.QuestCompany.OneQuset.set() #Дописать
    elif msg.text == 'Частным лицом':
        await msg.answer('Есть ли у вас название?')
        await QuestStorge.QuestGroup.OneQuset.set() #Дописать
   # await msg.answer('',reply_markup=types.ReplyKeyboardRemove())

    #await msg.answer('',reply_markup=types.ReplyKeyboardRemove()) 
#@dp.message_handler(text = '')

'''

def CloseKB(message: types.Message) -> None:
    message.answer('',reply_markup=types.ReplyKeyboardRemove())
    
@dp.message_handler(content_types=['text'], state=QuestStatesGroupTwo.QuestZero)
async def loung_QuseFour(msg: types.Message, state: FSMContext) -> None:
    await msg.answer('')
    async with state.proxy() as data:
        data['QuestZero'] = msg.text
    await QuestStatesGroupTwo.next()
'''


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)