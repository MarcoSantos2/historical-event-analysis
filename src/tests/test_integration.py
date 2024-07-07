import unittest
from src.app import app

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form action="/echo_user_input" method="POST">', response.data)
        self.assertIn(b'<input name="user_input">', response.data)
        self.assertIn(b'<input type="submit" value="Submit!">', response.data)

if __name__ == "__main__":
    unittest.main()
