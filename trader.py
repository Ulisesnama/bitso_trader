#%%
from time import time, sleep
import requests

url = "https://api.bitso.com/v3/trades/?book=btc_mxn"

prev_price = 0
min_to_buy = 1125000
while True:
    response = requests.get(url)
    response_json = response.json()
    response_payload = response_json.get('payload', [])
    last_op = response_payload[0]

    book = last_op.get('book', "")
    movement = last_op.get('maker_side', "")
    price = float(last_op.get('price', 0))
    happen = "UP" if price >= prev_price else "DOWN"
    print(f'${price} {happen} {book[:3]} {movement}')
    if price <= min_to_buy:
        while True:
            print("BUY")
    prev_price = price
    sleep(60 - time() % 60)
# %%
