from PyPDF2 import PdfReader
import os
import telebot
from helpful_funcs import gen_markup


telegram_token = str(os.environ['shpargalkin_bot'])
bot = telebot.TeleBot(telegram_token)


path = r"C:\Users\1\PycharmProjects\shpargalkin_bot\math"
dirs = os.listdir(path)  # содержит имена всех файлов в папке


def find_qstn(message):

    usr_inpt = str(message.text).lower()
    usr_inpt = "".join(c for c in usr_inpt if c.isalpha() or c == ' ')
    usr_inpt = set(usr_inpt.split())

    ref_to_qstn = ''
    mx_cmmn = 0

    for i in dirs:
        try:
            reader = PdfReader(fr"C:\Users\1\PycharmProjects\shpargalkin_bot\math\{i}")
            text = ((reader.pages[0].extract_text())[:150]).replace('-\n', '').replace('.', ' ').replace(',', ' ').replace('\n', ' ').lower()
            s1 = "".join(c for c in text if c.isalpha() or c == ' ')
            s1 = set(s1.split())
            if mx_cmmn < len(list(s1 & usr_inpt)):
                mx_cmmn = len(list(s1 & usr_inpt))
                ref_to_qstn = fr"C:\Users\1\PycharmProjects\shpargalkin_bot\math\{i}"
        except Exception as e:
            bot.send_message(993945655, str(e))

    try:
        bilet = open(ref_to_qstn, 'rb')
        bot.send_document(message.chat.id, bilet, reply_markup=gen_markup())
    except Exception as e:
        bot.send_message(993945655, str(e))
        bot.send_document(message.chat.id, 'Билета с такими словами не нашлось, введите больше слов'
                                           ' или проверьте правильность написания!', reply_markup=gen_markup())


def find_crtn_qstn(message):

    file = str(message.text)

    try:
        ref_to_qstn = fr"C:\Users\1\PycharmProjects\shpargalkin_bot\math\{file}.pdf"
        bilet = open(ref_to_qstn, 'rb')
        bot.send_document(message.chat.id, bilet, reply_markup=gen_markup())
    except Exception as e:
        bot.send_message(message.chat.id, str(e), reply_markup=gen_markup())
