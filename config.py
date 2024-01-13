#Configuration settings
#
#Osman Elias 1/12/2024


class Config:
    # Base configuration settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
    