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