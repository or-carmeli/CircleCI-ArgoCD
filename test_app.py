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
        url = "http://0.0.0.0:5000"
        for _ in range(30):
            if is_website_reachable(url):
                return
            time.sleep(1)
        self.fail(f"Website not reachable at {url}")

if __name__ == "__main__":
    unittest.main()

