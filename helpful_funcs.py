from telebot.types import ReplyKeyboardMarkup

def gen_markup():
    markup = ReplyKeyboardMarkup()
    buttons = ["Найти билет по словам", "Я знаю какой билет мне нужен!"]
    markup.resize_keyboard = True
    markup.add(*buttons)
    return markup