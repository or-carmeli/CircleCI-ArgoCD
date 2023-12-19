import requests
import unittest
import time

def is_website_reachable(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as err:
        print(f"Oops: {err}")
        return False
    
class TestWebsiteReachable(unittest.TestCase):

    def test_website_reachable(self):
        time.sleep(5)
        url = "http://flask_container:5000"  # Use the container name as the domain.
        self.assertTrue(is_website_reachable(url))

if __name__ == "__main__":
    unittest.main()

