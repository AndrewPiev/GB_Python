import telebot
from datetime import datetime as dt

token = '5816905204:AAF1gXD46dtmmzw_6qw2XtkF7dY1YHGiiTo'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton ('Как работать с комплексными числами:')
    itembtn2 = telebot.types.KeyboardButton ('Как работать с вещественными числами:')
    markup.add(itembtn1, itembtn2)
    bot.send_message(chat_id=message.chat.id, text='<b>Привет! Я бот-калькулятор! Если хочешь что-то вычислить, то пиши мне. Не забывай. что на ноль делить нельзя! Для более подробной справки жми на кнопки? если кнопок вдруг не стало видно, а они нужны, снова жми /start ;)))</b>', reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def calc(message):
    if message.text == 'Как работать с комплексными числами:':
        bot.send_message(message.chat.id, 'Для произведения операции над комплексными числами необходимо записывать их в формате (a+bj), где j - это мнимая единица. Так например для произвдения двух комплексных чисел необходимо записать (a+bj)*(c+dj). Удачных вычислений!')
    elif message.text == 'Как работать с вещественными числами:':
        bot.send_message(message.chat.id, 'Для произведения операции над вещественными числами необходимо просто записать в строке бота сами числа и необходимую операцию, не забывая об основновных правилах, например введя в строку (4+5)**2-71 Вы получите 10 так как сначала выполнится операция в скобках, потом возведение в степень, а потом уже вычитание')
    else:
        result = eval(message.text)
        bot.send_message(message.chat.id, result)
        time = dt.now().strftime('%H:%M')
        with open ('log.txt', 'a', encoding='utf-8') as file:
            file.writelines(f'Время операции: {time}, Операция: {message.text}, Результат операции: {result}\n')

bot.polling(none_stop=True)