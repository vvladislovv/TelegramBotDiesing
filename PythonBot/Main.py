from aiogram import Bot, Dispatcher,executor, types
from dotenv import load_dotenv
import os
from aiogram.types import ReplyKeyboardMarkup
from Button import kb_btns,kb_linkBtns,buyMain


BotAPI = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=BotAPI)


@dp.message_handler(commands=['start'])
async def NewUserOpenKB(message: types.Message) -> None:
    await message.answer('Привет!')
    
@dp.message_handler(text=['Убрать кнопки'])
async def CloseKB(message: types.Message) -> None:
    await message.answer('',reply_markup=types.ReplyKeyboardRemove())
    
# Партфолио
@dp.message_handler(text = 'Ознакомиться с портфолио')
async def conctacts1(message: types.Message):
    TextTable = [
        'Навигация по Telegram-каналу 📌',
        'Переходи ниже по ссылке!'
    ]
    await message.answer(text='\n'.join(TextTable),reply_markup=kb_linkBtns)


@dp.message_handler(text = 'Прайс услуг')
async def conctacts1(message: types.Message):
    await message.answer('t', reply_markup=buyMain) # написать текст 
    
@dp.callback_query_handler()
async def vote_callBack(callBack: types.CallbackQuery):
    if callBack.data == 'Услуги':
        await callBack.answer()
    
@dp.message_handler(text = 'Сделать заказ')
async def conctacts2(message: types.Message):
    await message.answer(f'Покупать товар у него @111')

   
if __name__ == "__main__":
    executor.start_polling(dp)