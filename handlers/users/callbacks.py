'''CALLBACKLARNI ILADIGAN HANDLERLAR'''
from telebot.types import CallbackQuery
from data.loader import bot


# def _status(id):
#     return bot.get_chat_member(-1001816297921, id).status
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def start(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     # print(chat_id)
#     status = ["creator"]
#     try:
#         if str(_status(chat_id)) in status:
#             bot.send_message(chat_id, 'Kanalga obuna')
#         else:
#             bot.send_message(chat_id, 'obuna emas')
#     except Exception as e:
#         print(e)
