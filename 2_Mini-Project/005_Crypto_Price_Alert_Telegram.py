"""
Mini Project (2): Cryptocurrency Price Alert with Telegram Notification

Step 1: Create a Data Structure that holds your alert requirements
- Define a data structure to store cryptocurrency details.
- Include 'lower_bound' and 'upper_bound' for each cryptocurrency.

Example:
cryptocurrencies = {
    "XRP": {
        "lower_bound": 25000,
        "upper_bound": 30000,
    },
    "ETH": {
        "lower_bound": 1500,
        "upper_bound": 2000,
    },
}

Step 2: Create a While Loop
- Use a while loop to continuously monitor cryptocurrency prices.

Step 3: Loop Through Each Cryptocurrency
- Use a for loop to iterate through the data structure.
- For each cryptocurrency, retrieve its current price.

Step 4: Check Price Conditions
- Compare the current price to the 'lower_bound' and 'upper_bound'.
- If the price is below the lower bound or above the upper bound:
    - Send an alert message using a Telegram bot.

Step 5: EXTRA (Optional Enhancements)
- Use try-except blocks to handle errors, such as API failures.
- Follow proper naming conventions for variables and functions.
- Add a delay between iterations using time.sleep() to avoid API rate limits.
"""

URL = 'https://api.mybitx.com/api/1/ticker?pair=XRPMYR'

"""
XRP: https://api.mybitx.com/api/1/ticker?pair=XRPMYR
ETH: https://api.mybitx.com/api/1/ticker?pair=ETHMYR
SOL: https://api.mybitx.com/api/1/ticker?pair=SOLMYR

Notice the endpoint? Make it dynamic to something like this: -

f'https://api.mybitx.com/api/1/ticker?pair={symbol}MYR'
"""

import requests
import time

TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = '540041214'

cryptocurrencies = {
    "XRP": {
        "lower_bound": 25000,
        "upper_bound": 30000,
    },
    "ETH": {
        "lower_bound": 1500,
        "upper_bound": 2000,
    },
    "SOL": {
        "lower_bound": 1000,
        "upper_bound": 2000,
    }
}

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

def crypto(symbol):
    url = f'https://api.mybitx.com/api/1/ticker?pair={symbol}MYR'
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()['last_trade'])


while True:
    time.sleep(1)
    for key, value in cryptocurrencies.items():
        price = crypto(key)
        print(price)
        print(value['lower_bound'])
        print(value['upper_bound'])
        if price > value['lower_bound'] and price < value['upper_bound']:
            send_message(key + ' buy now!')
        
