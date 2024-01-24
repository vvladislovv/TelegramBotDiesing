from aiogram import Router, F
from aiogram.types import Message
from Button.Inline import kb_linkBtns,buyMain
from Main.JsonFile import TextTable
import time

router = Router()


@router.message_handler(content_types=['text'])
async def ContextCheck(msg: Message):
    if msg.text == 'Ознакомиться с портфолио':
        TextTable.TextPortfolio()
        await msg.answer(text='\n'.join(TextTable),reply_markup=kb_linkBtns)
        
    elif msg.text == 'Прайс услуг':
        TextTable.MainMenuText()
        await msg.answer(text='\n'.join(TextTable), reply_markup=buyMain)
        
    elif msg.text == 'Сделать заказ':
        await msg.answer(f'Сейчас мне надо задать тебе пару вопросов')
        time.sleep(0.5)
        await msg.answer('Вы являетесь компанией или частным лицом?',reply_markup=Btny)