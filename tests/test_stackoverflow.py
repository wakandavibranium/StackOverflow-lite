import unittest

# Third-party imports
from flask_testing import TestCase

# Local imports
from app import create_app, db


class TestBase(TestCase):

    def create_app(self):

        # pass in the testing configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='postgresql://postgres:12345@localhost:5432/test_db')
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # create all tables
        db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """

        # drop all tables
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_user_can_signup(self):
        """
        Test that a user can create an account
        """

        response = self.client().post(
            '/api/v1/auth/signup/',
            data={
                'email': 'johndoe@gmail.com',
                'username': 'johndoe',
                'first_name': 'john',
                'last_name': 'doe',
                'password_hash': '12345'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('johndoe@gmail.com', str(response.data))


if __name__ == '__main__':
    unittest.main()
