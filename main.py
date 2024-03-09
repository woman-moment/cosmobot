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
    btn2 = types.KeyboardButton("Посмотреть объекты!")
    btn3 = types.KeyboardButton("Пройти квест!")
    markup.add(btn1, btn2, btn3)
    if message.from_user.last_name != None:
        mess = f'Приветик:), <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    else:
        mess = f'Приветик:), <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def another_commands(message):
    if message.from_user.id not in dict:
        dict[message.from_user.id] = 0
    num = dict[message.from_user.id]
    if message.text == 'Супер! Я готов!' or message.text == 'Я нашёл, дальше!': #проходим квест
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Я нашёл, дальше!")
        markup.add(btn1)
        if num == 13:
            finish(message)
        else:
            mess = f'Отлично, лови следующий объект:'
            bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
            #bot.forward_message(message.chat.id, idd, num)
            bot.copy_messages(message.chat.id, idd, arr[num])
            dict[message.from_user.id] += 1


    elif message.text == "Посмотреть объекты!" : #смотрим основные штуки
        mess = f'Отлично, лови:'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.copy_messages(message.chat.id, idd, arr[0])
        bot.copy_messages(message.chat.id, idd, arr[4])
        bot.copy_messages(message.chat.id, idd, arr[8])
        bot.copy_messages(message.chat.id, idd, arr[12])


    elif message.text == "Что умеет этот бот?":
        bot.copy_message(message.chat.id, idd, 23)


    elif message.text == "Пройти квест!":
        kvest(message)


    else: #сюда приходим в каждой непонятной ситуации
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что умеет этот бот?")
        btn2 = types.KeyboardButton("Посмотреть объекты!")
        btn3 = types.KeyboardButton("Пройти квест!")
        markup.add(btn1, btn2, btn3)
        mess = f'Выбирай, что хочешь делать:'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


def kvest(message):
    if message.from_user.id not in dict:
        dict[message.from_user.id] = 0
    dict[message.from_user.id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Супер! Я готов!")
    btn2 = types.KeyboardButton("В другой раз")
    markup.add(btn1, btn2)
    if message.from_user.last_name != None:
        mess = f'<b>{message.from_user.first_name} {message.from_user.last_name}, готов погулять по Самаре и посмотреть её космические объекты? </b>' \
               f'Я буду присылать тебе по одному объекту Самары космической, а ты должен будешь искать их в городе. Под спойлером в сообщении будет скрываться ' \
               f'адрес этого объекта, поэтому, если ты не так хорошо знаешь город, то, считай, этот адрес - моя подсказка тебе. Как только находишь объект, сообщай мне об этом - ' \
               f'нажимай кнопку "Я нашёл, дальше!" и лови новый объект. Объекты расположены таким образом, чтобы тебе было удобно передвигаться от каждого из них до следующего, и чтобы в ' \
               f'результате прохождения квеста ты обошёл весь город. <b>Готов?) Желаю тебе удачи!</b>'
    else:
        mess = f'<b>{message.from_user.first_name}, готов погулять по Самаре и посмотреть её космические объекты? </b>' \
               f'Я буду присылать тебе по одному объекту Самары космической, а ты должен будешь искать их в городе. Под спойлером в сообщении будет скрываться ' \
               f'адрес этого объекта, поэтому, если ты не так хорошо знаешь город, то, считай, этот адрес - моя подсказка тебе. Как только находишь объект, сообщай мне об этом - ' \
               f'нажимай кнопку "Я нашёл, дальше!" и лови новый объект. Объекты расположены таким образом, чтобы тебе было удобно передвигаться от каждого из них до следующего, и чтобы в ' \
               f'результате прохождения квеста ты обошёл весь город. <b>Готов?) Желаю тебе удачи!</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

def finish(message):
    if message.from_user.id not in dict:
        dict[message.from_user.id] = 0
    dict[message.from_user.id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что умеет этот бот?")
    btn2 = types.KeyboardButton("Посмотреть объекты!")
    btn3 = types.KeyboardButton("Пройти квест!")
    markup.add(btn1, btn2, btn3)
    if message.from_user.last_name != None:
        mess = f'Отлично, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, ' \
           f'ты молодец, прекрасно справился и смог найти все объекты!' \
           f'Надеюсь, квест тебе понравился:)'
    else:
        mess = f'Отлично, <b>{message.from_user.first_name} </b>, ' \
               f'ты молодец, прекрасно справился и смог найти все объекты!' \
               f'Надеюсь, квест тебе понравился:)'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

