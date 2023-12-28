from flask import Flask, jsonify
from stock_utils import get_real_time_stock_data
from stock_utils import get_stock_chart_data

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello !"

@app.route('/api/stock/<symbol>') #Dynamic path for any stock symbol
def stock_data(symbol):
    data = get_real_time_stock_data(symbol)
    return jsonify(data)

@app.route('/api/stock/chartdata/<symbol>')
def stock_chart_data(symbol):
    chart_data = get_stock_chart_data(symbol)  # Function from stock_utils.py
    return jsonify(chart_data)

if __name__ == "__main__":
    app.run(debug=True)


