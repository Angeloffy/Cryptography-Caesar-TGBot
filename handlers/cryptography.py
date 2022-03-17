from importlib.resources import contents
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import sys
sys.path.append("/TelegramBotAio/")
from create_bot import dp 

class FSMTest(StatesGroup):
    text = State()
    key = State()


# @dp.message_handler(commands="Зашифровать", state=None)
async def code_text(message: types.Message):
    await FSMTest.text.set()
    await message.reply('Введите текст для зашифровки')

# @dp.message_handler(content_types=['text'], state=FSMTest.text)
async def code_textGet(message: types.Message, state: FSMTest):
    async with state.proxy() as data:
        data['text'] = message.text
        await FSMTest.next()
        await message.reply('чек')

