import requests

api_key = "5eab0b3b130c52fee46949ac7b8800c4"

city = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print("Weather:", description)
    print("Temperature:", temperature, "Celsius")
else:
    print("Error fetching weather data.")