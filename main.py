import telebot
from telebot import types# для указание типов
import config

bot = telebot.TeleBot('7165523324:AAEIvwFPprEFi5shFyyYhDCStuvRZczgU1s')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что умеет этот бот?")
    btn2 = types.KeyboardButton("Посмотреть основные объекты!")
    btn3 = types.KeyboardButton("Пройти квест!")
    markup.add(btn1, btn2, btn3)
    mess = f'Приветик:), <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def another_commands(message):
    if(message.text == "Посмотреть основные объекты!"):
        bot.forward_message(message.chat.id, message.chat.id, message.message_id)
    elif(message.text == "Что умеет этот бот?"):
        bot.forward_message(message.chat.id, message.chat.id, message.message_id)
    elif (message.text == "Я устал:("):#если пользователь устал ходить по квесту, то заканчиваем
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что умеет этот бот?")
        btn2 = types.KeyboardButton("Посмотреть основные объекты!")
        btn3 = types.KeyboardButton("Пройти квест!")
        markup.add(btn1, btn2, btn3)
        mess = f'Ничего страшного, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, в следующий раз продолжишь!'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    else:
        mess = f'Приветик:), <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')


    

bot.polling(none_stop=True)
