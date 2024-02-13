from flask import Flask, jsonify, request, render_template, redirect, url_for
from extensions import db, jwt, login_manager  # Import from extensions.py
from flask_login import current_user, login_user, login_required, logout_user 
import os
from config import DevelopmentConfig
from stock_utils import get_real_time_stock_data, get_stock_chart_data

#User Model
from models import User

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    

    db.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated: #Checking for current user
            return redirect(url_for('home'))
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                return 'Invalid username or password'
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('home'))
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

             # Check if the username or email address already exists in the database
            existing_username = User.query.filter_by(username=username).first()
            existing_email = User.query.filter_by(email=email).first()
        
            if existing_username:
                return 'Username is already in use. Please choose a different one.'
            elif existing_email:
                return 'Email address is already in use. Please choose a different one.'

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))

        return render_template('register.html')

    @app.route('/api/stock/<symbol>') #Dynamic path for any stock symbol
    @login_required
    def stock_data(symbol):
        data = get_real_time_stock_data(symbol)
        return jsonify(data)

    @app.route('/api/stock/chartdata/<symbol>')
    @login_required
    def stock_chart_data(symbol):
        chart_data = get_stock_chart_data(symbol)  # Function from stock_utils.py
        return jsonify(chart_data)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)