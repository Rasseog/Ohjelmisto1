# weather.py
import requests

API_KEY = "5eab0b3b130c52fee46949ac7b8800c4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_for_airport(airport: dict) -> dict:
    """
    Hakee ajantasaisen sään lentokentän koordinaateilla.

    airport:
    {
        "icao": "EFHK",
        "name": "Helsinki Vantaa Airport",
        "city": "Helsinki",
        "lat": 60.3172,
        "lon": 24.9633
    }
    """
    params = {
        "lat": airport["lat"],
        "lon": airport["lon"],
        "appid": API_KEY,
        "units": "metric",
        "lang": "en",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather_main = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]

        # Pelin kulutuskerroin säästä
        if weather_main == "Clear":
            label = "Clear"
            multiplier = 1.0
        elif weather_main == "Clouds":
            label = "Cloudy"
            multiplier = 1.1
        elif weather_main in ("Drizzle", "Rain"):
            label = "Rain"
            multiplier = 1.3
        elif weather_main in ("Thunderstorm", "Snow"):
            label = "Storm"
            multiplier = 1.6
        else:
            label = weather_main
            multiplier = 1.2

        return {
            "label": label,
            "multiplier": multiplier,
            "temperature": temperature,
            "wind_speed": wind_speed,
            "description": description,
        }

    except requests.RequestException:
        return {
            "label": "Unknown",
            "multiplier": 1.2,
            "temperature": None,
            "wind_speed": None,
            "description": "weather unavailable",
        }