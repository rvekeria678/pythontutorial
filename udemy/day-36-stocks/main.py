from config import STOCK, COMPANY_NAME, AV_URL, NEWSAPI_URL, EMAIL_PORT, EMAIL_TIMEOUT
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os, requests, smtplib

load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def strong_growth(stock: str):
    parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol":stock,
        "outputsize":'compact',
        "apikey":os.environ['AV_API_KEY']
    }

    response = requests.get(url=AV_URL, params=parameters, timeout=120)
    response.raise_for_status()

    stock_data = response.json()
    if 'Information' in stock_data: return True
    dates = list(stock_data['Time Series (Daily)'].keys())
    first_close = float(stock_data['Time Series (Daily)'][dates[1]]['4. close'])
    second_close = float(stock_data['Time Series (Daily)'][dates[6]]['4. close'])
    difference = abs(first_close-second_close)
    return (difference / first_close) >= 0.05

if strong_growth(stock=STOCK):
    parameters = {
        'q': COMPANY_NAME,
        "from":str((datetime.now()-timedelta(days=3)).date()),
        "to":str(datetime.now().date()),
        "pageSize":3,
        "language":"en",
        "apiKey":os.environ['NEWS_API_KEY']
    }
    response = requests.get(url=NEWSAPI_URL, params=parameters,timeout=120)
    response.raise_for_status()

    article_data = response.json()
    articles = article_data['articles']

    content = ''
    for article in articles:
        content += f"Headline:{article['title']}\nBrief:{article['content']}\nLink:{article['url']}\n\n"

    with smtplib.SMTP('smtp.gmail.com', port=EMAIL_PORT, timeout=EMAIL_TIMEOUT) as connection:
        connection.starttls()
        connection.login(user=os.environ['EMAIL'], password=os.environ['PASSWORD'])
        connection.sendmail(from_addr=os.environ['EMAIL'], to_addrs=os.environ['EMAIL'], msg=f"Subject:{COMPANY_NAME} : {STOCK} [Alert]\n\n{content}".encode('utf-8'))

    


