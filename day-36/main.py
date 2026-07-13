import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "STOCKSAPIKEY"
NEWS_API_KEY = "NEWSAPIKEY"
account_sid = os.environ.get("AUTH_TOKEN")
auth_tocken = os.environ.get("AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
#TODO 2. - Get the day before yesterday's closing stock price
before_data = data_list[1]
before_closing_price = float(before_data["4. close"])
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_diff = before_closing_price - yesterday_closing_price
up_down = None
if stock_diff < 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
stock_diff_percent = round((stock_diff / before_closing_price) * 100)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(stock_diff_percent) > 5:
    print("Get news")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    news_data = news_response.json()["articles"]
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = news_data[:3]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{stock_diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    

#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(account_sid, auth_tocken)

    for article in formatted_articles:
        message = client.messages \
            .create(
                    body=article,
                    from_="+",
                    to="+"
                )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

