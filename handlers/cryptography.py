from keyboards import kb_cryptographyMode, kb_cryptographyKey, kb_cryptographyText, kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher 
import sys
from cv2 import split
sys.path.append("/TelegramBotAio/scripts")
from Caesar_Cipher import caesarCipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
class FSMTest(StatesGroup):
    metod = State()
    key = State()  
    text = State()

async def code_start(message: types.Message):
    await FSMTest.metod.set()
    await message.reply('Введите метод!', reply_markup=kb_cryptographyMode)

async def code_metod(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'encrypt':
            data['metod'] = message.text
            await message.reply('Введи ключ!', reply_markup=kb_cryptographyKey)
            await FSMTest.next()
        elif message.text == 'decrypt':
            data['metod'] = message.text
            await message.reply('Введи ключ!', reply_markup=kb_cryptographyKey)
            await FSMTest.next()
        else:
            await message.reply('Вы должны выбрать encrypt (зашифровать) или decrypt (разшифровать)')

async def code_key(message: types.Message, state: FSMContext):
    if message.text.isnumeric() == False:
        await message.reply('Ключем должна быть цифра!')
    elif int(message.text) > 66:
        await message.reply('Ключ должен быть от 1 до 66')
    elif int(message.text) < 0:
        await message.reply('Ключ должен быть от 1 до 66')
    else: 
        async with state.proxy() as data:
            data['key'] = message.text
        await FSMTest.next()
        await message.reply('Теперь введи текст', reply_markup=kb_cryptographyText)

async def code_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    async with state.proxy() as data:
        await message.answer(caesarCipher(str(data['metod']), int(data['key']), data['text']), reply_markup=kb_client)
    await state.finish()

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply('Done')


def register_handlers_cryptography(dp: Dispatcher):
    dp.register_message_handler(code_start, commands=["Шифр"], state=None)
    dp.register_message_handler(code_metod, state=FSMTest.metod)
    dp.register_message_handler(code_key, state=FSMTest.key)
    dp.register_message_handler(code_text, state=FSMTest.text)
    dp.register_message_handler(cancel_handler, state="*", commands='Отмена')