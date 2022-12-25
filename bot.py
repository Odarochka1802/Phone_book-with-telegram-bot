import telebot
from telebot import types
import cord as s
import logger as lg
import init_bd as b


token = "5912567534:AAH7VYXVeIgmDDxVrk7ZdrOnz8fQ1K0wurc"
bot = telebot.TeleBot(token, parse_mode='MARKDOWN')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - начать сначала (перезапустить бота)\n/main - главное меню\n/help - вызвать справку')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Помощь")
    btn2 = types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(
        message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Помощь"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        btn2 = types.KeyboardButton("Помощь")
        btn3 = types.KeyboardButton("Меню")
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(
        message.from_user), reply_markup=markup)
        

    elif (message.text == "Меню"):
        #bot.send_message(message.chat.id, f'Выбери пункт меню, введя соответствующую команду: ')
        b.init_data_base('base_phone.csv')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Показать все записи")
        btn2 = types.KeyboardButton("Найти номер по фамилии")
        btn3 = types.KeyboardButton("Поиск по номеру телефона")
        btn4 = types.KeyboardButton("Добавить новую запись")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выбери пункт меню, введя соответствующую команду:", reply_markup=markup)

    elif (message.text == "Показать все записи"):
        lg.logging.info('The user has selected item number 1')
        bot.send_message(message.chat.id, f'{s.retrive()}')

    elif message.text == "Найти номер по фамилии":
        lg.logging.info('The user has selected item number 2')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, find_surname)

    elif message.text == "Поиск по номеру телефона":
        lg.logging.info('The user has selected item number 3')
        bot.send_message(message.chat.id, f'Введите номер  телефона')
        bot.register_next_step_handler(message, find_number)

    elif message.text == "Добавить новую запись":
        lg.logging.info('The user has selected item number 4')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Показать все записи")
        button2 = types.KeyboardButton("Найти номер по фамилии")
        button3 = types.KeyboardButton("Поиск по номеру телефона")
        button4 = types.KeyboardButton("Добавить новую запись")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)




name_it = ''
surname_it = ''
number_it = ''

def find_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{s.retrive(surname=surname_it)}')


def find_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{s.retrive(number=number_it)}')


def get_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'Введите фамилию')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'Введите номер телефона')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    s.create(name_it, surname_it, number_it)
    bot.send_message(message.chat.id, f'Контакт успешно добавлен!')


print('server start')
bot.polling(none_stop=True)
