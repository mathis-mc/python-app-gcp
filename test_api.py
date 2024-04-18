import unittest
import app
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("API_KEY")

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_api(self):
        api_call = app.MakeApiCall(f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={key}")
        self.assertIsNotNone(api_call, "Should exist")

if __name__ == '__main__':
    unittest.main()