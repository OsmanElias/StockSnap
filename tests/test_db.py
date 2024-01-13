#To test database
#
#Osman Elias 1/12/2024

import unittest
from app import create_app, db
from models import User
from config import TestConfig  # Import the TestConfig

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        # Create an instance of app with the testing configuration
        self.app = create_app(config_class=TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Create a new database 

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Drop the database 
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        queried_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, 'test@example.com')

if __name__ == '__main__':
    unittest.main()