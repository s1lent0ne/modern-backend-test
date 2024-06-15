import requests
import datetime
import sys
import time
from dotenv import load_dotenv
import os

# Завантажуємо змінні з .env файлу
load_dotenv()

API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

# Перевірка наявності API_KEY
if not API_KEY:
    print("Помилка: Змінна середовища OPEN_WEATHER_API_KEY не знайдена. Перевірте файл .env.")
    sys.exit(1)

# Функція для отримання координат місця
def get_location_coordinates(location):
    geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={API_KEY}'
    response = requests.get(geocoding_url)
    data = response.json()

    # Перевірка, чи знайдено місце
    if not data:
        raise ValueError("Не вдалося знайти місцезнаходження. Будь ласка, перевірте правильність вводу.")

    location_data = data[0]
    lat = location_data['lat']
    lon = location_data['lon']
    city_name = location_data.get('name', 'Unknown')
    country = location_data.get('country', 'Unknown')
    return lat, lon, city_name, country

# Функція для отримання погодних даних
def get_weather_data(lat, lon, dt):
    URL = 'http://api.openweathermap.org/data/3.0/onecall/timemachine'
    params = {
        'lat': lat,
        'lon': lon,
        'dt': dt,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(URL, params=params)
    data = response.json()
    return data

# Функція для розрахунку середньої температури за останні 7 днів
def get_average_temperature(location):
    lat, lon, city_name, country = get_location_coordinates(location)

    total_temp = 0
    count = 0
    for days_ago in range(1, 8):
        dt = int(time.mktime((datetime.datetime.now() - datetime.timedelta(days=days_ago)).timetuple()))
        data = get_weather_data(lat, lon, dt)

        if 'data' in data and len(data['data']) > 0:
            temp = data['data'][0]['temp']
            total_temp += temp
            count += 1
        else:
            raise ValueError(f"Немає даних для {dt}. Відповідь API: {data}")

    if count == 0:
        raise ValueError("Не вдалося отримати дані про погоду за останні 7 днів.")

    avg_temp = total_temp / count
    return avg_temp, city_name, country

# Основний блок коду
if __name__ == "__main__":
    # Перевірка правильності кількості аргументів командного рядка
    if len(sys.argv) != 2:
        print("Використання: python weather_parser.py <назва міста>")
        sys.exit(1)

    city = sys.argv[1]

    try:
        avg_temp, found_city, found_country = get_average_temperature(city)
        print(f"Середня температура за останні 7 днів у місті {found_city}, {found_country}: {avg_temp:.2f}°C")
    except Exception as e:
        print(f"Помилка: {e}")