import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])
    else:
        print("Error")

except requests.exceptions.RequestException:
    print("Error")
