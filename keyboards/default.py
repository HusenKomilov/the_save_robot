'''
SIZ BU YERDA ODDIY KNOPKALAR YARATA OLASIZ
'''

from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    tiktok = KeyboardButton('TikTok')
    instagram = KeyboardButton('Instagram')
    call = KeyboardButton('👨🏻‍💻Creator')

    markup.add(tiktok, instagram, call)
    return markup
