import requests
from config import *
import time
import telebot

bot = telebot.TeleBot("6563970004:AAHYzwJZpactq2WimvxFG7xEkGF4OT6FRiM")


# переменная-флаг для обозначения появления товара
exist = False

# переменная для текста сообщения
textBot = ""

while True:
    for product, url_request in url_requests:
        exist = False
        response = requests.post(url_request)

        if "cartButtonEnabled" in response.json():
            exist = response.json()["cartButtonEnabled"]
            textBot = "появился товар - " + product
        else:
            print("error in check response json with status = ", response.status_code)

        if exist:
            bot.send_message(chat_id=-1002122887170, text=textBot)

    time.sleep(10)