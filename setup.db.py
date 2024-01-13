#Script to create the database
#
#Osman Elias 1/12/2024

from app import db  # app and db are defined in app.py
from models import User, OtherModel
from .. import app  # Import all models

with app.app_context():
    db.create_all()