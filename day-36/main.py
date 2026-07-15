"""
Day 36 - Stock Trading News Alert
Checks a stock's price change vs the previous close; if it moves
more than 5% in either direction, fetches the top 3 news headlines
about the company and sends them as an SMS via Twilio.
"""
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "your_alphavantage_key"
NEWS_API_KEY = "your_newsapi_key"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((abs(difference) / yesterday_closing_price) * 100, 2)

if diff_percent > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
        for article in articles
    ]

    client = Client("your_twilio_sid", "your_twilio_auth_token")
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+1_your_twilio_number",
            to="+1_your_verified_number",
        )
