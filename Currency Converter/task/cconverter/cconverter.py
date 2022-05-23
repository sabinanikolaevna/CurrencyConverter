import requests
import json
currency_code = input()
response = requests.get(f'http://www.floatrates.com/daily/{currency_code}.json')
rates = response.json()
cache = {}
if currency_code != 'usd' and currency_code != 'eur':
    usd = rates['usd']
    eur = rates['eur']
    cache['usd'] = usd
    cache['eur'] = eur
elif currency_code == 'usd':
    eur = rates['eur']
    cache['eur'] = eur
elif currency_code == 'eur':
    usd = rates['usd']
    cache['usd'] = usd

while True:
    exchange_currency = input()
    if len(exchange_currency) == 0:
        break
    amount = input()
    print("Checking the cache...")
    if exchange_currency in cache:
        print("Oh! It is in the cache!")
        information = cache[exchange_currency]
        rate = information['rate']
        result = round((float(rate) * float(amount)), 2)
        print(f'You received {result} {exchange_currency.upper()}.')
    elif exchange_currency not in cache:
        print("Sorry, but it is not in the cache!")
        exch_currency = rates[exchange_currency]
        cache[str(exchange_currency)] = exch_currency
        information = cache[exchange_currency]
        rate = information['rate']
        result = round((float(rate) * float(amount)), 2)
        print(f'You received {result} {exchange_currency.upper()}.')
