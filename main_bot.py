import telebot
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    url = 'https://www.citilink.ru/product/smartfon-apple-iphone-13-pro-a2483-128gb-zelenyi-3g-4g-6-1-ios-15-802-1809134/'
    driver.get(url)
    elem = driver.find_elements(By.XPATH, '//div[@class="ProductPrice ProductPrice_default ProductPrice_size_xs "]')
    #result_price = elem[0].find_elements(By.TAG_NAME, "span")[1].get_attribute("innerText").strip()
    result_price = 1
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра: '+str(result_price))
bot.polling()


