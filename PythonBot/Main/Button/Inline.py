from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
kb_linkBtns = InlineKeyboardMarkup()
buyMain = InlineKeyboardMarkup()

ButonStart1 = InlineKeyboardButton('Telegram Channel', url="https://t.me/kme_arts/1698")

kb_linkBtns.add(ButonStart1)


# buy buttons
buyButton1 = InlineKeyboardButton('Визитка',callback_data='Визитка')
buyButton2 = InlineKeyboardButton('Сертификат',callback_data='Сертификат')
buyButton3 = InlineKeyboardButton('Пост',callback_data='Пост')
buyButton4 = InlineKeyboardButton('Афиша',callback_data='Афиша')
buyButton5 = InlineKeyboardButton('Оформление группы VK',callback_data='группы')
buyButton6 = InlineKeyboardButton('Оформление YouTube канала',callback_data='Оформление')
buyButton7 = InlineKeyboardButton('Оформление презентации',callback_data='презентации')
buyButton8 = InlineKeyboardButton('Логотип',callback_data='Логотип')
buyButton9 = InlineKeyboardButton('Логобук',callback_data='Логобук')
buyButton10 = InlineKeyboardButton('Брендбук',callback_data='Брендбук')
buyButton11 = InlineKeyboardButton('Услуги нет',callback_data='Услуги')


buyMain.add(buyButton1,buyButton2,buyButton3)
buyMain.add(buyButton4,buyButton5,buyButton6)
buyMain.add(buyButton7,buyButton8,buyButton9)
buyMain.add(buyButton10,buyButton11)

