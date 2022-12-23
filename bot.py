import telebot
import cord as s
import logger as lg
import init_bd as b



token = "5810824593:AAEdGFS3eCFr882V8Q2jnJoLmZRINb_7xV0"
bot = telebot.TeleBot(token, parse_mode='MARKDOWN')


@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'Я тебя не понимаю. Введи: /Помощь.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, *{message.from_user.first_name}!*\nВ любой непонятной ситуации введи\nкоманду: /help\nЧтобы вызвать главное меню введи: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - начать сначала (перезапустить бота)\n/main - главное меню\n/help - вызвать справку')


name_it = ''
surname_it = ''
number_it = ''

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
        bot.send_message(message.chat.id, f'Выбери пункт меню, введя соответствующую команду: \n1 - Показать все записи.\n2 - Найти номер по фамилии.\n3 - Поиск по номеру телефона.\n4 - Добавить новую запись.')
        b.init_data_base('base_phone.csv')

    elif message.text == '1':
        lg.logging.info('The user has selected item number 1')
        bot.send_message(message.chat.id, f'{s.retrive()}')

    elif message.text == '2':
        lg.logging.info('The user has selected item number 2')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, find_surname)


    elif message.text == '3':
        lg.logging.info('The user has selected item number 3')
        bot.send_message(message.chat.id, f'Введите номер  телефона')
        bot.register_next_step_handler(message, find_number)

    elif message.text == '4':
        lg.logging.info('The user has selected item number 4')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)


    else:
        bot.send_message(
            message.chat.id, f'Я тебя не понимаю. Введи: /Помощь.')
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
bot.infinity_polling()
