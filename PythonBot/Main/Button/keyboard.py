from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_btns = ReplyKeyboardMarkup(resize_keyboard=True)
Btny = ReplyKeyboardMarkup(resize_keyboard=True)

ButonStart11 = KeyboardButton('Ознакомиться с портфолио')
ButonStart2 = KeyboardButton('Прайс услуг')
ButonStart3 = KeyboardButton('Сделать заказ')

kb_btns.add(ButonStart11)
kb_btns.row(ButonStart3, ButonStart2)


butt1 = KeyboardButton('Компанией')
butt2= KeyboardButton('Частным лицом')

Btny.add(butt1,butt2)