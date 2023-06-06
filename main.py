import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

import threading
import time

load_dotenv()

url = requests.get('https://coinmarketcap.com/es/currencies/bnb/')

soup = BeautifulSoup(url.content, 'html.parser')

result = soup.find("div",class_="priceValue").get_text()



def telegram_bot_sendtext(bot_message):
    
    bot_token = os.getenv('bot_token')
    bot_chatID = os.getenv('bot_chatID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    




# Tarea a ejecutarse cada determinado tiempo.
def timer():
    while True:
        test = telegram_bot_sendtext(f"El precio de BNB el dia de hoy es: {result} USD")
         
        time.sleep(5)   # 3 segundos.
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()
