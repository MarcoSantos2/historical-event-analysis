import unittest
from src.app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_echo_input(self):
        response = self.app.post('/echo_user_input', data={'user_input': 'Hello, Flask!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You entered: Hello, Flask!', response.data)

if __name__ == "__main__":
    unittest.main()
