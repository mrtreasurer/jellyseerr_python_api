import unittest
import requests

from http import HTTPStatus


class TestAuth(unittest.TestCase):
    # def test_api(self):
    #     response = requests.get("http://localhost:5055/api/v1", headers={"X-Api-Key": ""})
    #     self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_login(self):
        payload = {
            "username": "admin",
            "password": "password"
        }
        response1 = requests.post("http://jellyseerr:5055/api/v1/auth/jellyfin", json=payload)
        self.assertEqual(response1.status_code, HTTPStatus.OK)

        response2 = requests.get("http://jellysseerr:5055/api/v1", headers={"X-Api-Key": response1.json()["jellyfinAuthToken"]})
        print(response2.json())
        self.assertEqual(response2.status_code, HTTPStatus.OK)

if __name__ == "__main__":
    unittest.main()
