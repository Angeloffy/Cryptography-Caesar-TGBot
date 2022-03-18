from aiogram import types, Dispatcher
from keyboards import kb_client
async def ping(message: types.Message):
    await message.answer("pong".format(message.from_user))

async def command_start(message: types.Message):
    await message.answer("Привет!".format(message.from_user), reply_markup=kb_client)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(ping, commands=["ping"]) 
    dp.register_message_handler(command_start, commands=['start']) 