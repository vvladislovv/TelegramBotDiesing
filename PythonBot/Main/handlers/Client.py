
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from Main.JsonFile import TextTable

StorageMemary = MemoryStorage()
BotAPI = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=BotAPI,storage=StorageMemary)

@dp.message_handler(commands=['start', 's'])
async def NewUserOpenKB(message: Message) -> None:
    TextTable.StartText()
    await message.answer(text='\n'.join(TextTable),reply_markup=kb_btns)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)