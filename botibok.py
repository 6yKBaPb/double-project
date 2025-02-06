import telebot, os, random, requests, bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
from telebot import types

A = 1
B = 0
bot = telebot.TeleBot("7225494481:AAGIImEPG32zZWBSCRncqBnyRjH5XMgQ5zk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Шалом, я экобот! Ты здесь что бы узнать экологическое состояние своего региона, не так ли? Но сначала...")
    bot.reply_to(message, "Пройдём небольшой тест?")
    bot.reply_to(message, "Напиши /121")

@bot.message_handler(commands=['121'])
def send_startest(message):
    bot.reply_to(message, "Проверка пройдена!")
    bot.reply_to(message, "Список доступных команд - /menu")


@bot.message_handler(commands=['menu'])
def send_comands(message):
    if A==1:
        bot.reply_to(message, "Выберете регион:\n/1 - Самарская область\n/2 - Московская область\n/3 - Краснодарский край")

@bot.message_handler(commands=['1'])
def send_samara(message):
    bot.reply_to(message, "Выберете то, что хотите изучить:\n \n/Новости1\nактуальные новости в мире экологии\n \n/Климат1 \nлокальный климат и прогнозы вашего региона\n \n/Челендж\nежедневный челендж. Присоединяясь к нему, вы вностие свой вклад.")

@bot.message_handler(commands=['2'])
def send_moscow(message):
    bot.reply_to(message, "Выберете то, что хотите изучить:\n \n/Новости2\nактуальные новости в мире экологии\n \n/Климат2 \nлокальный климат и прогнозы вашего региона\n \n/Челендж\nежедневный челендж. Присоединяясь к нему, вы вностие свой вклад.")

@bot.message_handler(commands=['3'])
def send_krasnodar(message):
    bot.reply_to(message, "Выберете то, что хотите изучить:\n \n/Новости3\nактуальные новости в мире экологии\n \n/Климат3 \nлокальный климат и прогнозы вашего региона\n \n/Челендж\nежедневный челендж. Присоединяясь к нему, вы вностие свой вклад.")

@bot.message_handler(commands=['Новости1'])
def send_samaraN(message):
    f = open('images/bd-02-2025.jpg', 'rb')
    bot.send_photo(message.chat.id, f)
    f.close()
    bot.reply_to(message, "В данный момент ведется работа по обновлению инфраструктуры накопления ТКО. "
    "\nНа ближайшую трехлетку Правительством региона принято решение об опережающем финансировании закупки контейнеров и ремонту старых."
    "\nНа эти цели заложено 861 млн. руб. Планируется отремонтировать и обустроить почти 3 000 контейнерных площадок, закупить более 12 тысяч мусоросборников. "
    "На указанные цели заложено 861 миллион рублей. Новыми контейнерными площадками будут пользоваться 434 782 жителей региона. "
    "При этом в 2024 году было выделено муниципалитетам 324 млн. руб. на приобретение 6 861 мусоросборников, устройство 182 контейнерных площадок и ремонт 806."
    "\n \nИсточник: https://xn----8sbaal4aminob4aj4nmb.xn--p1ai/reforma/\n \nВернуться в меню: /menu")

@bot.message_handler(commands=['Новости2'])
def send_moscowN(message):
    bot.reply_to(message, "Приключение через науку: откройте для себя экологию вместе со столичными экоцентрами\n"
                "С 6 по 10 февраля экоцентры Департамента природопользования и охраны окружающей среды города Москвы"
                "проведут тематические мероприятия в рамках Дня российской науки. Традиционно этот праздник отмечается 8 февраля.\n \n"
                "Подробнее: https://www.mos.ru/news/item/149738073/\n \nВернуться в меню: /menu")

@bot.message_handler(commands=['Новости3'])
def send_krasnodyarN(message):
    bot.reply_to(message, "Обострение экологической ситуации на Кубани: что происходит с мазутом в Черном море два месяца спустя\n"
                "Два месяца спустя после аварии танкеров в Черном море, на побережье Краснодарского края обнаружены новые выбросы мазута."
                "Экологи предупреждают, что объемы загрязнения сопоставимы с первоначальной аварией, и если не принять срочных мер, последствия могут распространиться далеко за пределы региона.\n \n"
                "Подробонее: https://ura.news/news/1052885093\n \nВернуться в меню: /menu")

@bot.message_handler(commands=['Климат1'])
def send_moscowP(message):
    f = open('images/weatherRS.jpg', 'rb')
    bot.send_photo(message.chat.id, f)
    f.close()
    bot.reply_to(message, "Прогноз погоды на ближайшие дни в Самаре.\n \nПодробнее: https://yandex.ru/pogoda/samara?utm_source=serp&utm_campaign=helper&utm_medium=desktop&utm_content=helper_desktop_main&utm_term=title&lat=53.195876&lon=50.100199\n \nВернуться в меню: /menu")

@bot.message_handler(commands=['Климат2'])
def send_moscowP(message):
    f = open('images/weatherRM.jpg', 'rb')
    bot.send_photo(message.chat.id, f)
    f.close()
    bot.reply_to(message, "Прогноз погоды на ближайшие дни в Москве.\n \nПодробнее: https://yandex.ru/pogoda/moscow?ysclid=m6thhkl2ek755500526\n \nВернуться в меню: /menu")

@bot.message_handler(commands=['Климат3'])
def send_krasnodyarP(message):
    f = open('images/weatherRK.jpg', 'rb')
    bot.send_photo(message.chat.id, f)
    f.close()
    bot.reply_to(message, "Прогноз погоды на ближайшие дни в Краснодаре.\n \nПодробнее: https://yandex.ru/pogoda/krasnodar?ysclid=m6thld3wo8614119473\n \nВернуться в меню: /menu")

@bot.message_handler(commands=['Челендж'])
def send_chellange(message):
    f = open('images/sled.jpg', 'rb')
    bot.send_photo(message.chat.id, f)
    f.close()
    bot.reply_to(message, "Челендж на 06.02.2025:\n \nНе использовать средства передвижения, работающие на двигателе внутреннего сгорания. Лёгкий способ что бы уменьшить свой и общественный углеродный след. \nПройдитесь пешком!\n \nВернуться в меню: /menu")

bot.polling()










