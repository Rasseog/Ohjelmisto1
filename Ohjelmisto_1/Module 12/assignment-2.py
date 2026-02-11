import requests

api_key = "YOUR_API_KEY_HERE"

municipality = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print("Error")

except requests.exceptions.RequestException:
    print("Error")
