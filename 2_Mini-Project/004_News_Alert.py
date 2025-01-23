"""
Mini Project (1): Telegram Alert for New News on TheEdge

Objective:
Build a script that monitors news updates from TheEdge API and sends a Telegram alert whenever new news is detected.

Step 1: Initialize Data Storage
- Create an empty list to store news items.

Step 2: Fetch Initial Data
- Run the API for the first time to fetch the current news.
- Store the fetched news data in the list.

Step 3: Continuous Monitoring
- Use a while loop to re-run the API periodically to check for updates.

Step 4: Detect New News
- Compare the newly fetched news with the existing data in the list.
- If there is a news item not already in the list, it indicates new news.

Step 5: Send Alerts
- When new news is detected:
    - Send an alert to your Telegram bot.
    - Add the new news item(s) to the list to keep it up-to-date.

Optional Enhancements:
- Use time.sleep() to add a delay between API calls and avoid overwhelming the API.
- Log news updates for future reference.
- Use try-except to handle API errors gracefully.
- Add a mechanism to stop the loop after a certain number of checks or based on user input.


API Endpoint: https://theedgemalaysia.com/api/loadMoreCategories?offset=0&categories=malaysia
    - This API gives latest 10 data from the news category 'malaysia'.
    - You can change the offset to get more data.
    - offset=0 gives the latest data.
    - offset=10 gives the next 10 data.

"""

import requests

TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = 'YOUR_CHAT_ID'

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

