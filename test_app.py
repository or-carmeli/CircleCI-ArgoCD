import unittest
import requests

class TestWebsiteReachable(unittest.TestCase):
    def test_website_reachable(self):
        url = "http://flask_container:5000"  # Use the container name as the domain.
        try:
            response = requests.get(url, timeout=10)  # Added timeout for safety
            self.assertEqual(response.status_code, 200, f"Website not reachable at {url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.fail(f"Website not reachable at {url}. Error: {e}")

if __name__ == "__main__":
    unittest.main()

