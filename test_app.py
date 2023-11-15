import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def test_fetch_weather_data(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
