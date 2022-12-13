'''KOMANDALARNI ILADIGAN HANDLERLAR'''

from telebot.types import Message
from data.loader import bot
from keyboards.default import main_menu
from .text_handlers import creator


@bot.message_handler(commands=['start'], chat_types='private')
def start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    text = f"✋Привет <b>{first_name}</b>,\n я скачиваю видео и картинки с Tik Tok и Instagram!"
    bot.send_message(chat_id, text, reply_markup=main_menu())


@bot.message_handler(content_types=['text', 'audio', 'video', 'sticker', 'animations'])
def echo(message: Message):
    chat_id = message.chat.id
    arl = message.text
    if arl.startswith('https://'):
        text = "👇Выберите один из разделов ниже"
        bot.send_message(chat_id, text, reply_markup=main_menu())
    elif arl.startswith("👨🏻‍💻Creator"):
        return creator
    else:
        bot.copy_message(chat_id, chat_id, message.message_id)
