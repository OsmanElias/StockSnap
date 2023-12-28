# stock_utils.py
import requests
import os

def get_real_time_stock_data(symbol):
    api_key = os.getenv("STOCK_API_KEY")  # Ensure the environment variable is correctly set
    function = "TIME_SERIES_INTRADAY"  # or another function based on your requirement
    interval = "15min"  # Interval can be 1min, 5min, 15min, 30min, 60min
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}"
    response = requests.get(url)
    return response.json()

def get_stock_chart_data(symbol):
    api_key = os.getenv("STOCK_API_KEY")  # API Key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=compact"

    response = requests.get(url)
    data = response.json()

    # Process and transform data into a format suitable for Chart.js
    chart_data = []
    for date, price_info in data['Time Series (Daily)'].items():
        chart_data.append({
            'date': date,
            'price': float(price_info['4. close'])  # Adjust based on needed price type
        })

    return chart_data