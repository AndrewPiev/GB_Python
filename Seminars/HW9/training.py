# a = '+ 7.2 6.3 5.5 7.7'
# b = a.split(' ')
# print (b)

# print (eval('(1+2j)/(3+4j)'))
# print (eval('(3+4)'))



# import telebot

# token = '5588260408:AAHvUYTT-8NKDFt-jX0BRuL0172r32Dp94A'

# bot = telebot.TeleBot(token)


# word = 'Андрей'
# name = 'БА! Знакомые все лица!'
# @bot.message_handler(content_types=['text'])

# def echo(message):
#     if word in message.text:
#         bot.send_message(message.chat.id, name)
#     else:
#      bot.send_message(message.chat.id, message.text)
# bot.polling(none_stop=True)


# from datetime import datetime
# import telebot
# from pycbrf import ExchangeRates

# bot = telebot.TeleBot('5816905204:AAF1gXD46dtmmzw_6qw2XtkF7dY1YHGiiTo')

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
#     itembtn1 = telebot.types.KeyboardButton ('Как работать с комплексными числами')
#     itembtn2 = telebot.types.KeyboardButton ('Как работать с действительными числами')
#     markup.add(itembtn1, itembtn2)
#     bot.send_message(chat_id=message.chat.id, text='<b>Привет! Это калькулятор для действительных и комплексных чисел. Жми кнопку для справки!</b>', reply_markup=markup, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def message(message):
#     message_norm = message.text.strip().lower()

#     if message_norm in ['usd', 'eur', 'cny', 'chf', 'gbp', 'jpy']:
#         rates = ExchangeRates(datetime.now())
#         bot.send_message(chat_id=message.chat.id, text = f'<b>Today {message_norm.upper()} rate is {float(rates[message_norm.upper()].rate)}RUR</b>', parse_mode = 'html')

# bot.polling(non_stop=True)