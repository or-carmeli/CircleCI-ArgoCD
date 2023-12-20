import unittest
import requests

class TestWebsiteReachable(unittest.TestCase):
    def test_website_reachable(self):
        url = "http://flask-app:5000"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Website not reachable at {url}")

if __name__ == '__main__':
    unittest.main()
