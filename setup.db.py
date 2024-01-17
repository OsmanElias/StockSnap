#Script to create the database
#
#Osman Elias 1/12/2024

from app import create_app, db
from models import User # Import all necessary models

app = create_app()  # Create an instance of the Flask app

with app.app_context():
    db.create_all()  # Create database tables
    