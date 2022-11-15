import telebot
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_SHIM', None)
browser = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()


