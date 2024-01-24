from aiogram import Router, F
from aiogram.types import CallbackQuery

routre = Router()

@routre.callback_query()
async def MessageCallBack(Cbk: CallbackQuery):
    if Cbk.data == 'Услуги':
        await Cbk.message.answer(text="Вашей услуги нет в списке? Напишите мне лично, и мы обсудим то, что вам нужно @kondrachuk_me")

