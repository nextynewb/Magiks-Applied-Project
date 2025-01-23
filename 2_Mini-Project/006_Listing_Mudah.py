
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

TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = 'YOUR_CHAT_ID'

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

