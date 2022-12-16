'''
BOTNI ISHGA TUSHIRISH UCHUN KERAK BO'LADIGAN NARSALARNI KIRG'IZING
'''
from telebot import TeleBot
from telebot.types import BotCommand
from config import TOKEN

bot = TeleBot(TOKEN, use_class_middlewares=True, parse_mode='html')

bot.set_my_commands(commands=[
    BotCommand('/start', "Перезапустите бота🔄")
])
