
"""
Mini Project (3): Mudah Listing Alert

Step 1: Create a Data Structure
- Define a Data Structure for Listing Alerts.

Example:

alerts = [
    {
        "name": "Macbook Pro",
        "price": 5000,
    },
    {
        "name": "Macbook Air",
        "price": 4000,
    }
]

Step 2: Create a While Loop
- Use a while loop to continuously monitor the listings.

Step 3: Loop Through Each Alert
- Use a for loop to iterate through the data structure.
- For each alert, retrieve the latest listing data.

Step 4: Check Price Conditions
- Compare the listing price to the alert price.
- If the listing price is below the alert price:
    - Send an alert message using a Telegram bot.

URL: https://search.mudah.my/v1/search?q={product_name}

Example:

Macbook Pro: https://search.mudah.my/v1/search?q=macbook%20pro
Macbook Air: https://search.mudah.my/v1/search?q=macbook%20air
"""


import requests
import json

api_url = f'https://search.mudah.my/v1/search?q={product_name}'
alerts = []


def get_listing_mudah(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        alerts.extend(data)
    else:
        print("Failed to get data from the API")

def get_latest_listing(alerts):
    for alert in alerts:
        return()
    
while True:
    product_name = "Macbook"
    response = requests.get(f'https://search.mudah.my/v1/search?q={product_name}')
    print(response.json())


import requests
import json
import time

TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = '677286250'

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

alert_products = [
    "Macbook Pro", "PS5"
]


all_items = []

for item in alert_products:
    product_name = item
    response = requests.get(f'https://search.mudah.my/v1/search?q={product_name}')
    data = response.json()['data']

    for x in data:
        url = x['attributes']['adview_url']
        all_items.append(url)

while True:
    for item in alert_products:
        product_name = item
        response = requests.get(f'https://search.mudah.my/v1/search?q={product_name}')
        data = response.json()['data']

        for x in data:
            url = x['attributes']['adview_url']
            if url in all_items:
                continue
            else:
                print(url)
                print('-----')
        
    time.sleep(10)



TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = 'YOUR_CHAT_ID'

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

