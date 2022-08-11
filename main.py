import telebot
from helpful_funcs import gen_markup
import os
from test import find_qstn, find_crtn_qstn

telegram_token = str(os.environ['shpargalkin_bot'])
bot = telebot.TeleBot(telegram_token)





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Удачи на контрольной точке!!!',
                     parse_mode='html', reply_markup=gen_markup())


@bot.message_handler()
def text_message_handler(message):
    match message.text:
        case "Найти билет по словам":
            sent = bot.send_message(message.chat.id, 'Напиши в следующем сообщении первые 8-15 слов')
            bot.register_next_step_handler(sent, find_qstn)
        case "Я знаю какой билет мне нужен!":
            sent = bot.send_message(message.chat.id, 'Напиши номер билета цифрами')
            bot.register_next_step_handler(sent, find_crtn_qstn)

bot.polling(none_stop=True)