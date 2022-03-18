from aiogram import Bot, Dispatcher
from cfg import TOKEN_BOT
from aiogram.contrib.fsm_storage.memory import MemoryStorage 

storage = storage=MemoryStorage()
bot = Bot(token = TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)