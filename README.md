# Weather Data Parser

Weather Data Parser - це Python-скрипт, який отримує погодні дані для зазначеного місця з публічного API, аналізує дані та обчислює середню температуру за останні сім днів. Скрипт приймає назву міста як вхідний параметр з командного рядка та виводить середню температуру з повідомленням.

## Вимоги

- Python 3.6+
- Віртуальне середовище Python (рекомендується)
- Бібліотека `requests`
- Бібліотека `python-dotenv`

## Встановлення

1. **Клонування репозиторію**

    ```bash
    git clone https://github.com/your-username/weather-data-parser.git
    cd weather-data-parser
    ```

2. **Створення та активація віртуального середовища**

    На Windows:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

    На Unix або MacOS:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Встановлення залежностей**

    ```bash
    pip install -r requirements.txt
    ```

4. **Створення `.env` файлу**

    Створіть файл `.env` у кореневій директорії проекту та додайте ваш API ключ:
    ```env
    OPEN_WEATHER_API_KEY=your_api_key_here
    ```

## Додаткова інформація
Цей проект використовує API [OpenWeather](https://openweathermap.org/api/one-call-3) для отримання погодних даних. 
Переконайтеся, що ви зареєструвалися на їхньому сайті та отримали API ключ.


## Приклад запуску

```bash
python weather_data_parser.py Kyiv
```


# Проект `find_second_largest.py`

Цей проект містить скрипт на Python, який знаходить друге за величиною значення у списку чисел.

## Вимоги

- Python 3.6 або вище

## Використання

Скрипт `find_second_largest.py` приймає список чисел, переданих через командний рядок, і повертає друге за величиною значення.

### Приклад запуску

```bash
python find_second_largest.py 3 1 4 1 5 9 2 6 5 3 5
