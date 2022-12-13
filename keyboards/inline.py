'''
SIZ BU YERDA INLINE KNOPKALAR YARATA OLASIZ
'''
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def creator():
    markup = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("CREATOR", url="https://t.me/huseynkomilov")
    markup.add(btn)
    return markup
