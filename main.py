import requests
from config import *
import time
import telebot
import copy

bot = telebot.TeleBot("6563970004:AAHYzwJZpactq2WimvxFG7xEkGF4OT6FRiM")



def get_order(file):
    """
    Функция перевода заказок из общего json-а в словарь премиум и обычных заказов. В словаре ключи - id заказов.
    Пример формата: { "id": "город А - город Б", "id": "город А - город Б" ...}
    :param file: json файл после парсинга страницы
    :return: словарь с обычными заказами, словарь с премиум заказами
    """
    array_simple = {}
    array_premium = {}
    file = file["loads"]
    for record in file:
        if "priority" not in record:
            array_simple[record["id"]] = record["loading"]["location"]["city"] + " -> " \
                                               + record["unloading"]["location"]["city"]
        else:
            array_premium[record["id"]] = record["loading"]["location"]["city"] + " -> " \
                                               + record["unloading"]["location"]["city"]
    return array_simple, array_premium




# подгружаем актуальные данные
response = requests.post(url_request, json=headers_array)
array_order_simple, array_order_priority = get_order(response.json())

# цикл постоянных проверок
while True:
    answer = ''
    response = requests.post(url_request, json=headers_array)
    try:
        array_order_simple_vr, array_order_priority_vr = get_order(response.json())
    except:
        continue
    for i in array_order_simple_vr:
        if i not in array_order_simple and i not in array_order_priority:
            answer += "<b>Появился новый маршрут:</b>\n" + array_order_simple_vr[i] + "\n" * 2
        if i in array_order_simple:
            break
    array_order_simple = copy.deepcopy(array_order_simple_vr)


    for i in array_order_priority_vr:
        if i not in array_order_priority and i not in array_order_simple:
            answer += "<b>Появился новый маршрут:</b>\n" + array_order_priority_vr[i] + "\n" * 2

        if i in array_order_priority:
            break
    array_order_priority = copy.deepcopy(array_order_priority_vr)

    if answer != '':
        bot.send_message(chat_id=-1002122887170, text=answer, parse_mode='HTML')

    time.sleep(60)
