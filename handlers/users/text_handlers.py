'''TEXTLARNI ILADIGAN HANDLERLAR'''
from telebot.types import Message
from data.loader import bot
from instagram_save import instagram_download
from tik_tok import tiktok_save


@bot.message_handler(regexp='Instagram')
def instagram(message: Message):
    chat_id = message.chat.id
    if message.text.startswith('https://www.instagram.com/'):
        link = message.text
        data = instagram_download(link=link)
        if data == "Bad":
            bot.send_message(chat_id, '❌В URL-адресе ошибка! \nПожалуйста, проверьте URL!')
        else:
            if data['type'] == 'video':
                bot.send_video(chat_id, video=data['media'], timeout=3)
            elif data['type'] == 'image':
                bot.send_photo(chat_id, photo=data['media'])
            elif data['type'] == 'carousel':

                for i in data['media']:
                    bot.send_video(chat_id, video=i)


@bot.message_handler(regexp='TikTok')
def tiktok(message: Message):
    chat_id = message.chat.id
    if message.text.startswith('https://www.tiktok.com/'):
        link = message.text
        date = tiktok_save(link=link)
        try:
            bot.send_video(chat_id, video=date['video'])
            bot.delete_message(chat_id, message.message_id)
        except:
            bot.send_message(chat_id, '❌В URL-адресе ошибка! \nПожалуйста, проверьте URL!')


@bot.message_handler(regexp="👨🏻‍💻Creator")
def creator(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     f"Создатель бота <a>@huseynkomilov</a> Свяжитесь с администратором для предложений и запросов!")
