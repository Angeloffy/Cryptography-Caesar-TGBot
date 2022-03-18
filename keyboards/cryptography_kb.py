from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b_cancel = KeyboardButton('/Отмена')
b1 = KeyboardButton('/Шифр')
b2 = KeyboardButton('encrypt')
b3 = KeyboardButton('decrypt')
b4 = KeyboardButton('5')
b4 = KeyboardButton('10')
b5 = KeyboardButton('20')
b6 = KeyboardButton('30')
b7 = KeyboardButton('Random')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1)

kb_cryptographyMode = ReplyKeyboardMarkup()
kb_cryptographyMode.add(b2).add(b3).add(b_cancel)

kb_cryptographyKey = ReplyKeyboardMarkup()
kb_cryptographyKey.add(b4).add(b5).add(b6).add(b_cancel)

kb_cryptographyText = ReplyKeyboardMarkup()
kb_cryptographyText.add(b7).add(b_cancel)