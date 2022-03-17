from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

# Main Menu

btnShifr = KeyboardButton("Шифр")
btnRandom = KeyboardButton('Рандомное число')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnShifr, btnRandom)

shifrMake = KeyboardButton("/shifr")
shifrDemake = KeyboardButton("/Разшифровать")
shifrMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(shifrMake, shifrDemake, btnMain)