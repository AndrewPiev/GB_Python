from datetime import datetime
import telebot
from pycbrf import ExchangeRates

bot = telebot.TeleBot('5816905204:AAF1gXD46dtmmzw_6qw2XtkF7dY1YHGiiTo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = telebot.types.KeyboardButton ('USD')
    itembtn2 = telebot.types.KeyboardButton ('EUR')
    itembtn3 = telebot.types.KeyboardButton ('CNY')
    itembtn4 = telebot.types.KeyboardButton ('CHF')
    itembtn5 = telebot.types.KeyboardButton ('GBP')
    itembtn6 = telebot.types.KeyboardButton ('JPY')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(chat_id=message.chat.id, text='<b>Hello! Click or type the currency to see Exchange rates!</b>', reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur', 'cny', 'chf', 'gbp', 'jpy']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text = f'<b>Today {message_norm.upper()} rate is {float(rates[message_norm.upper()].rate)}RUR</b>', parse_mode = 'html')

bot.polling(non_stop=True)