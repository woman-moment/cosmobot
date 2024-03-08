import telebot
from telebot import types# для указание типов
import config

idd = -1002140770203
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
    if(message.text == 'Супер! Я готов!'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Я нашёл! Дальше)")
        markup.add(btn1)
        bot.forward_message(message.chat.id, idd, 5)
        mess = f'Ура, ты дошла до сюда, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
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
    elif (message.text == "Пройти квест!"):
        kvest(message)
    else:
        mess = f'Приветик:), <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')


def kvest(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Супер! Я готов!")
    btn2 = types.KeyboardButton("В другой раз")
    markup.add(btn1, btn2)
    mess = f'Ничего страшного, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, в следующий раз продолжишь!'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
