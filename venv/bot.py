import sys
import logging
from aiogram import executor
from create_bot import dp
sys.path.append("/TelegramBotAio/")
from handlers import client, cryptography

cryptography.register_handlers_cryptography(dp)
client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True)