import requests
import time
import json

while(True):
    n = 0
    coin_input = input("Insert your prefered coin: ")
    user_input = input("Do you want to quit? y/n:")
    if user_input == 'y' or  user_input == 'n':
        if user_input != 'y':
            while n < 7:
                cotacao = requests.get("https://economia.awesomeapi.com.br/json/all")
                cotacao = cotacao.json()
                cotacao_coin = cotacao[coin_input]["bid"]
                print(cotacao_coin)
                time.sleep(1)
                n += 1
        else:
            print("Getting out of here!")
            break
    else:
        print("Invalid syntax")