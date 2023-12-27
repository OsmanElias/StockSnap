from flask import Flask, jsonify
from stock_utils import get_real_time_stock_data

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api/stock/<symbol>') #Dynamic path for any stock symbol
def stock_data(symbol):
    data = get_real_time_stock_data(symbol)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


