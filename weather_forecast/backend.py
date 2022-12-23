import requests
import constants


def get_data(location, forecast_days=None):
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={location}&" \
          f"appid={constants.OPEN_WEATHER_MAP_API_KEY}"
    response = requests.get(url)
    data = response.json()
    weather_data = data["list"]
    nr_obs = 8 * forecast_days
    filtered_weather_values = weather_data[:nr_obs]
    return filtered_weather_values


if __name__ == "__main__":
    print(get_data(location="Tokio", forecast_days=2))
