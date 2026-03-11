# weather.py
import requests

API_KEY = "5eab0b3b130c52fee46949ac7b8800c4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_for_airport(airport: dict) -> dict:
    """
    Hakee ajantasaisen sään lentokentän koordinaateilla.

    airport-esimerkki:
    {
        "icao": "EFHK",
        "name": "Helsinki Vantaa Airport",
        "city": "Helsinki",
        "lat": 60.3172,
        "lon": 24.9633
    }

    Palauttaa esim:
    {
        "label": "Rain",
        "multiplier": 1.3,
        "temperature": 12.4,
        "wind_speed": 6.1,
        "description": "light rain"
    }
    """
    lat = airport["lat"]
    lon = airport["lon"]

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        weather_main = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        temperature = data["main"]["temp"]

        # Yksinkertainen pelilogiikka kulutukselle
        if weather_main == "Clear":
            multiplier = 1.0
            label = "Clear"
        elif weather_main in ("Clouds",):
            multiplier = 1.1
            label = "Cloudy"
        elif weather_main in ("Drizzle", "Rain"):
            multiplier = 1.3
            label = "Rain"
        elif weather_main in ("Thunderstorm", "Snow"):
            multiplier = 1.6
            label = "Storm"
        else:
            multiplier = 1.2
            label = weather_main

        return {
            "label": label,
            "multiplier": multiplier,
            "temperature": temperature,
            "wind_speed": wind_speed,
            "description": description
        }

    except requests.RequestException:
        # Varasää jos API ei vastaa
        return {
            "label": "Unknown",
            "multiplier": 1.2,
            "temperature": None,
            "wind_speed": None,
            "description": "weather unavailable"
        }