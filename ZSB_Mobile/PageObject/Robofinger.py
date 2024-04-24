import requests
import time


class ServoAPI:
    def __init__(self, driver):
        self.driver = driver


def test_robo_finger():
    url = "http://10.233.194.77/servo?angle=0"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Robo finger set to 180 degree successful.")
    except requests.exceptions.RequestException as e:
        print("Failed to control robo finger. Exception: {e}")

    time.sleep(5)

    url = "http://10.233.194.59/servo?angle=0"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Robo finger set to 0 degree successful.")
    except requests.exceptions.RequestException as e:
        print("Failed to control robo finger. Exception: {e}")


if __name__ == "__main__":
    test_robo_finger()