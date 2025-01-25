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
import time

TELEGRAM_API = '7500850112:AAHZGnF83amv0bsBC0gSLuBTjyuteK7faIg'
CHAT_ID = 'YOUR_CHAT_ID'

def send_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)

news_collection = [742441, 742440, 742439, 742436, 742435, 742434, 742433, 742429, 742427, 742425, 742421, 742423, 742419, 742418, 742414, 742412, 742410, 742409, 742408, 742407, 742381, 742406, 742405, 742398, 742400, 742394, 742392, 742390]
params = {
"offset" : "0",
"categories" : "malaysia"}

url = "https://theedgemalaysia.com/api/loadMoreCategories?"


def get_news_data():
    for i in range (0,20):
        params["offset"] = str(i)
        offset = params["offset"]
        response = requests.get(url,params=params)
        if response.status_code ==200:
            try:
                data = response.json()["results"]
                for item in data:
                    news_id = item["nid"]
                    news_title = item["title"]
                    if news_id in news_collection:
                        return news_id, news_title, False
                        continue
                    else:
                        news_collection.append(news_id)
                        return news_id, news_title, True
            except:
                print("Cannot fetch data")    


while True:
    time.sleep(1)
    data_from_theedge = get_news_data()
    news_id, news_title, new_news = data_from_theedge
    if new_news == True:
        print(f'New news, title: {news_title}')
    else:
        print(f'I am sorry, you have caught up with all the news')




#thinking of automate this daily
#if the user can choose to get
"""
while True:
    request_news = input("Do you want to get the new news? (Y/N)").capitalize()
    if request_news == "Y":
        time.sleep(1)
        data_from_theedge = get_news_data()
        news_id, news_title, new_news = data_from_theedge
        if new_news == True:
            print(f'New news, title: {news_title}')
        else:
            print(f'I am sorry, you have caught up with all the news')
            break
    else:
        print("Thank you, please lmk if you want new news")
        break
    """
#thinking if we can get the most of the data is political news? investment news?
#thiknig if we only return news based on what we wanted, 

    


