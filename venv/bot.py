import sys
import logging
from aiogram import executor
from create_bot import dp
sys.path.append("/TelegramBotAio/")
from handlers import client

logging.basicConfig(level=logging.INFO)
client.register_handlers_client(dp)
executor.start_polling(dp, skip_updates=True)