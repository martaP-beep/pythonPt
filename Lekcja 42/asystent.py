import requests
from pprint import pprint

API_KEY = "91c53203b56228177ab8bb050a1cdd42"

def check_coordinates(city, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    print(response.status_code)
    pprint(response.json())
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]
    city = response.json()[0]["name"]
    country = response.json()[0]["country"]
    return lat, lon, city, country

def get_weather(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    print(response.status_code)
    pprint(response.json())
    humidity = response.json()["main"]["humidity"]
    temp = response.json()["main"]["temp"]
    pressure = response.json()["main"]["pressure"]
    return humidity, temp, pressure





print("Witaj, tutaj Twój asystent podróży")

origin_city = input("Wpisz nazwę miasta, z którego podróżujesz: ")
origin_lat,origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)

dest_city = input("Wpisz nazwę miasta, do którego podróżujesz: ")
dest_lat,dest_lon, dest_city, dest_country = check_coordinates(dest_city, API_KEY)


print(f"Podróżujesz z miasta {origin_city}")
print(f"Podróżujesz do miasta {dest_city}")

humidity, temp, pressure = get_weather(dest_lat, dest_lon)
# Wyświetl informacje o wilgotności powietrza, temperaturze 
# i ciśnieniu w miejscu docelowym podróży
