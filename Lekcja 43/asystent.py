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


def get_country_name(country_code):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code.upper()}")
    # print(response.status_code)
    # pprint(response.json())
    country_name = response.json()[0]["name"]["common"]
    return country_name

def get_currency_code(country_code):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code.upper()}")
    # pprint(response.json())
    currency_code =list(response.json()[0]["currencies"].keys())[0]
    return currency_code

def get_currency_ratio(currency1, currency2):
    if currency1 != "PLN":
        response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{currency1.lower()}/")
        # pprint(response.json())
        cur1_ratio = response.json()["rates"][0]["mid"]
    else: cur1_ratio = 1
    if currency2 != "PLN":
        response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{currency2.lower()}/")
        # pprint(response.json())
        cur2_ratio = response.json()["rates"][0]["mid"]
    else: cur2_ratio = 1

    return float(cur1_ratio) / float(cur2_ratio)



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
print(f"Wilgotność powietrza:  {humidity}")
print(f"Temperatura:  {temp}")
print(f"Ciśnienie:  {pressure}")

get_country_name(dest_country)
print(f"Kraj: {get_country_name(dest_country)}")

get_currency_code(dest_country)
print(f"Kod waluty w miejscu docelowym: {get_currency_code(dest_country)}")

print("Przelicznik walut pomiędzy walutą startową a docelową")
print(get_currency_ratio(get_currency_code(origin_country), get_currency_code(dest_country)))