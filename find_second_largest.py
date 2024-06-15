import sys

def find_second_largest(nums: list[int]) -> int:
    # Перевірка, чи список містить хоча б два елементи
    if len(nums) < 2:
        raise ValueError("Список повинен містити щонайменше два елементи")

    # Ініціалізація змінних для першого і другого максимальних значень
    first_max = float('-inf')
    second_max = float('-inf')
    found_second = False

    # Перебір елементів списку для знаходження першого і другого максимальних значень
    for num in nums:
        if num > first_max:
            second_max = first_max
            first_max = num
            found_second = True if second_max != float('-inf') else found_second
        elif second_max < num < first_max:
            second_max = num
            found_second = True

    # Якщо другого максимального значення не знайдено, повернути перше максимальне значення
    if not found_second:
        second_max = first_max

    return second_max


if __name__ == "__main__":
    # Отримання аргументів з командного рядка
    if len(sys.argv) < 2:
        print("Будь ласка, введіть список чисел через пробіл.")
        sys.exit(1)

    try:
        # Конвертація аргументів у список чисел
        nums = list(map(int, sys.argv[1:]))
        result = find_second_largest(nums)
        print(f"Друге за величиною значення: {result}")
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")