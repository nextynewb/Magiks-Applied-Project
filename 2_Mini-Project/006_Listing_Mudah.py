
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
import time

TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = '677286250'

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

alerts = [
    {
        "name" : "Macbook Pro",
        "price" : 5000
    },
    {
        "name" : "Macbook Air",
        "price" : 4000
    }
]


ad_urls = []
#get_adview_url

def get_adview_url(product_name):
    url = f'https://search.mudah.my/v1/search?q={product_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['data']
        for x in data:
            adview_url = x['attributes']['adview_url']
            if adview_url not in ad_urls:
                ad_urls.append(adview_url)
                return(adview_url)
    return None

def get_price(product_name):
    url = f'https://search.mudah.my/v1/search?q={product_name}'
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()['data']
        for x in data:
                price = x['attributes']['price']
                return(price)
    return None


while True:
    time.sleep(1)
    for item in alerts:
        watchlist = item['name']
        listing_price = get_price(watchlist)
        ad_url = get_adview_url(watchlist)
        alert_price = item['price']
        if listing_price < alert_price:
            print('-----')
            print(listing_price)
            print(f'buy {watchlist} at {ad_url} ----')
        