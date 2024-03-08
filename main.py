import telebot
from telebot import types# для указание типов
import config

dict = {}
arr = [[2, 3, 4], [5, 6], [7, 8], [9], [10, 11], [12], [13], [14, 15], [16], [17], [18], [19], [20, 21]]
idd = -1002140770203
bot = telebot.TeleBot('7165523324:AAEIvwFPprEFi5shFyyYhDCStuvRZczgU1s')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in dict:
        dict[message.from_user.id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что умеет этот бот?")
    btn2 = types.KeyboardButton("Cмотреть объекты!")
    btn3 = types.KeyboardButton("Пройти квест!")
    markup.add(btn1, btn2, btn3)
    mess = f'Приветик:), <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def another_commands(message):
    num = dict[message.from_user.id]
    if message.text == 'Супер! Я готов!' or message.text == 'Я нашёл! Дальше)': #проходим квест
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Я нашёл! Дальше)")
        markup.add(btn1)
        if num == 13:
            finish(message)
        else:
            mess = f'Отлично, лови следующий объект)'
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
            #bot.forward_message(message.chat.id, idd, num)
            bot.forward_messages(message.chat.id, idd, arr[num])
            dict[message.from_user.id] += 1


    elif message.text == "Посмотреть основные объекты!" : #смотрим основные штуки
        mess = f'Отлично, лови:'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.forward_messages(message.chat.id, idd, arr[0])
        bot.forward_messages(message.chat.id, idd, arr[4])
        bot.forward_messages(message.chat.id, idd, arr[8])
        bot.forward_messages(message.chat.id, idd, arr[12])


    elif message.text == "Что умеет этот бот?":
        bot.forward_message(message.chat.id, message.chat.id, message.message_id)


    elif message.text == "Пройти квест!":
        kvest(message)


    else: #сюда приходим в каждой непонятной ситуации
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что умеет этот бот?")
        btn2 = types.KeyboardButton("Посмотреть основные объекты!")
        btn3 = types.KeyboardButton("Пройти квест!")
        markup.add(btn1, btn2, btn3)
        mess = f'Выбирай, что хочешь делать:'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


def kvest(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Супер! Я готов!")
    btn2 = types.KeyboardButton("В другой раз")
    markup.add(btn1, btn2)
    mess = f'<b>{message.from_user.first_name} {message.from_user.last_name}</b>, готов полулять по Самаре и посмотреть её космические объекты?'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

def finish(message):
    dict[message.from_user.id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что умеет этот бот?")
    btn2 = types.KeyboardButton("Посмотреть основные объекты!")
    btn3 = types.KeyboardButton("Пройти квест!")
    markup.add(btn1, btn2, btn3)
    mess = f'Отлично, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, ' \
           f'ты молодец, прекрасно справился найти все объекты!' \
           f'Надеюсь, наш квест тебе понравился:)'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

#Исправить: добавить проверку, что если фамилия none то не надо её включать
# чтобы не показывалось, откуда переслано
# сделать асинхронным на разных устройствах
#исправить объект на 12 (ГОТОВО)