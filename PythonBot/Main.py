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

class QuestStatesGroup(StatesGroup):
    QuestZero = State()
    QuestOne = State()
    QuestTwo = State()
    QuestThree = State()
    QuestFour = State()


class QuestStatesGroupTwo(StatesGroup):
    QuestZero = State()
    QuestOne = State()
    QuestTwo = State()
    QuestThree = State()

Compp = False
NoCompp = False

# Quest Comp -- error bag key and lagier
@dp.message_handler(content_types=['text'], state=QuestStatesGroup.QuestZero)
async def loung_QuseFour(msg: types.Message, state: FSMContext) -> None:
    await msg.answer('Есть ли у вас название?')
    async with state.proxy() as data:
        data['QuestZero'] = msg.text
        print(data)
    await QuestStatesGroup.next()

@dp.message_handler(content_types=['text'], state=QuestStatesGroup.QuestOne)
async def loung_QuseFour(msg: types.Message, state: FSMContext) -> None:
    await msg.answer('Есть ли у вас название?')
    async with state.proxy() as data:
        data['QuestOne'] = msg.text
        print(data)
    await msg.answer('Что вы предлагаете своим клиентам?')
    await QuestStatesGroup.next()

@dp.message_handler(content_types=['text'], state=QuestStatesGroup.QuestTwo)
async def loung_QuseOne(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestTwo'] = msg.text
    await msg.answer('Какие у вас преимущества?')
    await QuestStatesGroup.next()

@dp.message_handler(content_types=['text'], state=QuestStatesGroup.QuestThree)
async def loung_QuseTwo(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestThree'] = msg.text
    await msg.answer('Какая аудитория с которой работает компания?')
    await QuestStatesGroup.next()

@dp.message_handler(content_types=['text'], state=QuestStatesGroup.QuestFour)
async def loung_QuseFour(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestFour'] = msg.text
        print(data)
    await msg.answer('Дизайн чего вам требуется?')
    await state.finish()


#Quest Coper
@dp.message_handler(content_types=['text'], state=QuestStatesGroupTwo.QuestZero)
async def loung_QuseOne(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestZero'] = msg.text
    await msg.answer('Что компания предлагает своим клиентам?')
    await QuestStatesGroupTwo.next()
    
@dp.message_handler(content_types=['text'], state=QuestStatesGroupTwo.QuestOne)
async def loung_QuseOne(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestOne'] = msg.text
    await msg.answer('Что компания предлагает своим клиентам?')
    await QuestStatesGroupTwo.next()

@dp.message_handler(content_types=['text'], state=QuestStatesGroupTwo.QuestTwo)
async def loung_QuseTwo(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestTwo'] = msg.text
    await msg.answer('Какие преимущества компании?')
    await QuestStatesGroupTwo.next()

@dp.message_handler(content_types=['text'], state=QuestStatesGroupTwo.QuestThree)
async def loung_QuseThree(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestThree'] = msg.text
    await msg.answer('Какая аудитория с которой работает компания?')
    await QuestStatesGroupTwo.next()

'''@dp.message_handler(content_types=['text'], state=QuestStatesGroupTwo.QuestFour)
async def loung_QuseFour(msg: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['QuestFour'] = msg.text
        print(data)
    await msg.answer('Дизайн чего вам требуется?')
    await state.finish()
'''

@dp.message_handler(commands=['start'])
async def NewUserOpenKB(message: types.Message) -> None:
    await message.answer('Привет!',reply_markup=kb_btns)
    
@dp.message_handler(text=['Убрать кнопки'])
async def CloseKB(message: types.Message) -> None:
    await message.answer('',reply_markup=types.ReplyKeyboardRemove())
    
# Партфолио
@dp.message_handler(text = 'Ознакомиться с портфолио')
async def conctacts1(message: types.Message):
    TextTable = [
        'Навигация по моему портфолио 📌',
        'Переходи ниже по кнопке'
    ]
    await message.answer(text='\n'.join(TextTable),reply_markup=kb_linkBtns)


@dp.message_handler(text = 'Прайс услуг')
async def conctacts1(message: types.Message):
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
        'Если услуги нет в списке - нажмите на кнопку Услуги неь',
    ]
    await message.answer(text='\n'.join(TextTable), reply_markup=buyMain) # написать текст 
    
@dp.callback_query_handler()
async def vote_callBack(callBack: types.CallbackQuery):
    if callBack.data == 'Услуги':
       await callBack.message.answer(text="Вашей услуги нет в списке? Напишите мне лично, и мы обсудим то, что вам нужно @kondrachuk_me")
    elif callBack.data == 'Компанией':
       # await callBack.message.answer('Какое название у вашей компании?')
        await QuestStatesGroupTwo.QuestOne.set()
    elif callBack.data == 'Частным':
        #await callBack.message.answer(text="Есть ли у вас название?")
        await QuestStatesGroup.QuestOne.set()

@dp.message_handler(text = 'Сделать заказ')
async def conctacts2(message: types.Message):
    await message.answer(f'Сейчас мне надо задать тебе пару вопросов')
    time.sleep(1)
    await message.answer('Вы являетесь компанией или частным лицом?',reply_markup=Btny)   

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)