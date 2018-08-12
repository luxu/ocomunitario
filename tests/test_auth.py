import unittest
import re
from app import create_app, db


class FlaskAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_and_login(self):
        # register new account
        response = self.client.post('/request/register', data={
            "first_name": "Marcus",
            "last_name": "Mann",
            "email": "marcus.mann@example.com",
            "password": "123456"
        })

        self.assertEqual(response.status_code, 302)

        # login with the new account
        response = self.client.post('/', data={
            'email': 'john@example.com',
            'password': 'cat'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 500)
        self.assertTrue(
            r"You should be redirected automatically to target URL: (\<a href=\"/\">/</a>.)  If not click the link\.\n 500",
            response.get_data(
                as_text=True))

        response = self.client.post('/', data={
            'email': 'marcus.mann@example.com',
            'password': '123456'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            re.search(
                r'Dashboard',
                response.get_data(
                    as_text=True)))
        self.assertTrue(
            re.search(
                r"(<title>Homepage.+</title>)",
                response.get_data(
                    as_text=True)))
