import requests

API_KEY = "352fec3489e0f7dc6715182f8eb5f847"
BASE_URL = "https://home.openweathermap.org/api_keys"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("error")