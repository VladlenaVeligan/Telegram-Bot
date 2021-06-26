import telebot
from telebot import types
from parsedata import parse, parseanime 

def readfile(file_name):
    with open (file_name, 'r') as file:
        return file.read()

bot = telebot.TeleBot(readfile('token.ini'))

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('Триллер')
    button2 = types.KeyboardButton('Фантастика')
    button3 = types.KeyboardButton('Комедия')
    button4 = types.KeyboardButton('Ужасы')
    button5 = types.KeyboardButton('Аниме')
    button6 = types.KeyboardButton('Драма')

    markup.add(button1, button2, button3, button4, button5, button6)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nКакой фильмец смотрим сегодня?😜'.format(message.from_user),
        parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types='[text]')
def film_choice(message):
    
    if message.chat.type == 'private':
        if message.text == 'Триллер':
            bot.send_message(message.chat.id, 'Смотрю кому-то захотелось понервничать\nВот, что у меня есть для тебя⤵️')
            bot.send_message(message.chat.id, parse('https://www.kinonews.ru/top100-thriller/'))
        elif message.text == 'Фантастика':
            bot.send_message(message.chat.id, '"На дворе был 2024 год, машины уже захватили панету..."\nВот, что подыскал⤵️')
            bot.send_message(message.chat.id, parse('https://www.kinonews.ru/top100-sci-fi/'))
        elif message.text == 'Комедия':
            bot.send_message(message.chat.id, 'Желаю посмеяться от души\nКое-что у меня для тебя найдется')
            bot.send_message(message.chat.id, parse('https://www.kinonews.ru/top100-comedy/'))
        elif message.text == 'Ужасы':
            bot.send_message(message.chat.id, 'Надеюсь ты решил посмотреть его не ночью...')
            bot.send_message(message.chat.id, parse('https://www.kinonews.ru/top100-horror/'))
        elif message.text == 'Аниме':
            bot.send_message(message.chat.id, 'Лови, надеюсь ты его еще не смотрел')
            bot.send_message(message.chat.id, parseanime('https://www.kinonews.ru/top100-anime/'))
        elif message.text == 'Драма':
            bot.send_message(message.chat.id, 'Не чего из-за чего погрусить в реальной жизни?\nВот держи, хороший повод поплакать⤵️')
            bot.send_message(message.chat.id, parse('https://www.kinonews.ru/top100-drama/'))
        else:
            bot.send_message(message.chat.id, 'Извини, я тебя не понимаю 😔')



bot.polling(none_stop=True)


