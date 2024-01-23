#Configuration settings
#
#Osman Elias 1/12/2024
import os


class Config:
    # Base configuration settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'


    

