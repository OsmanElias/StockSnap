#@app.route('/api/stock/<symbol>') #Dynamic path for any stock symbol
#def stock_data(symbol):
#    data = get_real_time_stock_data(symbol)
#    return jsonify(data)

#@app.route('/api/stock/chartdata/<symbol>')
#def stock_chart_data(symbol):
#   chart_data = get_stock_chart_data(symbol)  # Function from stock_utils.py
#    return jsonify(chart_data)


#Main file with routes included
#
#Osman Elias 1/12/2024

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import os
from config import DevelopmentConfig
from stock_utils import get_real_time_stock_data
from stock_utils import get_stock_chart_data

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'fallback-secret-key')

    db.init_app(app)
    jwt.init_app(app)

    @app.route('/')
    def home():
        return "Hello, Flask!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
