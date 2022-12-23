import requests
import constants


def get_data(location, days=None, option=None):
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={location}&" \
          f"appid={constants.OPEN_WEATHER_MAP_API_KEY}"
    print(url)
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(location="Tokio"))