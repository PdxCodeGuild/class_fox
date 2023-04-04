
import requests
import secrets

# requesting treasure island
# response = requests.get("https://www.gutenberg.org/cache/epub/120/pg120.txt")

# dummy json data
# response = requests.get("https://jsonplaceholder.typicode.com/todos/")
# todos = response.json()
# print(len(todos))

api_key = secrets.api_key

city = input("What city do you want weather for? ")
lat_lon_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
response = requests.get(lat_lon_url)
location_data = response.json()

lat = location_data[0]["lat"]
lon = location_data[0]["lon"]
weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"

response = requests.get(weather_url)
weather_data = response.json()
print(f'City: {weather_data["name"]}')
print(f'Current Temp: {weather_data["main"]["temp"]}˚F')
print(f'Description: {weather_data["weather"][0]["description"]}')
