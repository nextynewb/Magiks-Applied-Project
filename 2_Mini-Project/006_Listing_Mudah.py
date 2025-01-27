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

products = [["Macbook Pro",6000.0], ["Macbook Air",4000.0]]
ad_url = []


def get_data(product):
    url = f'https://search.mudah.my/v1/search?q={product}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['data']
            for attribute in data:
                price = float(attribute['attributes']['price'])
                ad_view = attribute['attributes']['adview_url']
                if ad_view in ad_url:
                    continue
                else:
                    ad_url.append(ad_view)
                    return price,ad_view
    except:
        print("There is an error fetching data from Mudah.my")
        return None, None

while True:
    time.sleep(1)
    for item in products:
        product = item[0]
        data_from_mudah = get_data(product)
        price_listing,ad_listing = data_from_mudah
        price_alert = item[1]
        if price_listing < price_alert:
            print(f"Yo! you should buy {product} with price {price_listing} at {ad_listing}")


