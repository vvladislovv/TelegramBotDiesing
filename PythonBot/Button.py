from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup

kb_btns = ReplyKeyboardMarkup(resize_keyboard=True)
kb_linkBtns = InlineKeyboardMarkup()

ButonStart1 = InlineKeyboardButton('Telegram Channel', url="https://t.me/kme_arts/1698")
ButonStart2 = KeyboardButton('Прайс услуг')
ButonStart3 = KeyboardButton('Сделать заказ')

kb_linkBtns.add(ButonStart1)
kb_btns.row(ButonStart3, ButonStart2)

buyMain = InlineKeyboardMarkup()
# buy buttons
buyButton1 = InlineKeyboardButton('Визитка — 2.500 рублей',callback_data='Визитка')
buyButton2 = InlineKeyboardButton('Сертификат — 3.000 рублей',callback_data='Сертификат')
buyButton3 = InlineKeyboardButton('Пост — 2.000 рублей',callback_data='Пост')
buyButton4 = InlineKeyboardButton('Афиша — 3.000 рублей',callback_data='Афиша')
buyButton5 = InlineKeyboardButton('Оформление группы VK — от 5.000 рублей',callback_data='группы')
buyButton6 = InlineKeyboardButton('Оформление YouTube канала — от 5.000 рублей',callback_data='Оформление')
buyButton7 = InlineKeyboardButton('Оформление презентации — от 5.000 рублей',callback_data='презентации')
buyButton8 = InlineKeyboardButton('Логотип — от 10.000 рублей',callback_data='Логотип')
buyButton9 = InlineKeyboardButton('Логобук — Цена обсуждается лично',callback_data='Логобук')
buyButton10 = InlineKeyboardButton('Брендбук — Цена обсуждается лично',callback_data='Брендбук')
buyButton11 = InlineKeyboardButton('Услуги нет в списке',callback_data='Услуги')


buyMain.add(buyButton1,buyButton2,buyButton3)
buyMain.add(buyButton4,buyButton5,buyButton6)
buyMain.add(buyButton7,buyButton8,buyButton9)
buyMain.add(buyButton10,buyButton11)

