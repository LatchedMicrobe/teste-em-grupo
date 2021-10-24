import requests
import time
import json

while(True):
    n = 0
    user_input = input("Do you want to quit? y/n:")
    if user_input == 'y' or  user_input == 'n':
        if user_input != 'y':
            while n < 7:
                cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
                cotacao = cotacao.json()
                cotacao_btc = cotacao["BTCBRL"]["bid"]
                print(cotacao_btc)
                time.sleep(1)
                n += 1
        else:
            print("Getting out of here!")
            break
    else:
        print("Invalid syntax")