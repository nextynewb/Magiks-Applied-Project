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
"""

ENDPOINT = 'https://theedgemalaysia.com/api/loadMoreCategories?offset=0&categories=malaysia'


"""
The URL will give 10 news data. Starting from offset - 10
"""
