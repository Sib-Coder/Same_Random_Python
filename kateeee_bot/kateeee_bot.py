import telebot
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import logging
import os


# Инициализация бота
token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)


def gettime():
    return str(datetime.now().time())

# Обработчик команды /time
@bot.message_handler(commands=['time'])
def handle_time(message):
    bot.send_message(message.chat.id, gettime())


def get_weather(city):
    url = f'https://www.google.com/search?q=погода+в+{city}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Парсинг температуры
        temperature = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
        # Парсинг описания погоды
        description = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text
    
        return f'Погода в городе {city}: {temperature}, {description}'
    else:
        return "Проблема с получением погоды( Простите госпожа ((("




# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я телеграм-бот Заливной Рыбы ❤️\nЯ могу тебе показать:\n/cat - котика\n/dog - пёсика\n/wether Название_города - погоду в городе")

# Обработчик команды /wether
@bot.message_handler(commands=['wether'])
def handle_wether(message):
    city = message.text.split()
    try:
        bot.send_message(message.chat.id, get_weather(city[1]))
    except (IOError, Exception) as e:
        logging.error("Ошибка передачи города", exc_info=True)
        bot.send_message(message.chat.id, "Передай мне город правильно")
    

#получение котиков
@bot.message_handler(commands=['cat'])
def send_cat_image(message):
    # Запрос к API для получения случайного изображения с котиком
    response = requests.get('https://api.thecatapi.com/v1/images/search')

    if response.status_code == 200:
        # Получаем URL изображения
        cat_image_url = response.json()[0]['url']
        # Отправляем изображение пользователю
        bot.send_photo(message.chat.id, cat_image_url)
    else:
        logging.warning("Не удалось получить изображение с котиком. Попробуйте позже.")
        bot.send_message(message.chat.id, "Не удалось получить изображение с котиком. Попробуйте позже.")


#выводит собачек
@bot.message_handler(commands=['dog'])
def send_dog_image(message):
    # Запрос к API для получения случайного изображения собаки
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    if response.status_code == 200:
        # Получаем URL изображения
        dog_image_url = response.json()['message']
        # Отправляем изображение пользователю
        bot.send_photo(message.chat.id, dog_image_url)
    else:
        logging.warning("Не удалось получить изображение собаки. Попробуйте позже.")
        bot.send_message(message.chat.id, "Не удалось получить изображение собаки. Попробуйте позже.")



def main():
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('Bot will be starting!')
    bot.polling()



if __name__=="__main__":
    main()