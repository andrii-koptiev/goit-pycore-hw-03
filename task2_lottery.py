"""
Завдання 2. get_numbers_ticket(min, max, quantity)

Функція генерує набір унікальних випадкових чисел для лотереї.

Параметри:
- min      — мінімальне можливе число у наборі (не менше 1).
- max      — максимальне можливе число у наборі (не більше 1000).
- quantity — кількість чисел, які потрібно вибрати
             (від 1 до max - min + 1, тобто в межах діапазону).

Вимоги:
- Повертає відсортований список унікальних випадкових чисел
  у межах [min, max].
- Якщо параметри не відповідають обмеженням — повертає пустий список [].
- Використовуйте модуль random (наприклад, random.sample).

Приклад: get_numbers_ticket(1, 49, 6) -> [4, 15, 23, 28, 37, 45]
"""

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    is_input_valid = validate_input(min, max, quantity)
    if not is_input_valid:
        return []

    lottery_numbers = random.sample((range(min, max + 1)), quantity)
    lottery_numbers.sort()
    return lottery_numbers


def validate_input(min: int, max: int, quantity: int) -> bool:
    return (
        min >= 1
        and max <= 1000
        and min <= max
        and quantity > 0
        and quantity < len((range(min, max + 1)))
    )


def ask_user(label: str, low: int, high: int, default: int) -> int:
    while True:
        hint = f"{low} - {high}, default {default}"
        raw = input(f" ? {label} ({hint}): ").strip()
        if raw == "":
            return default
        try:
            value = int(raw)
        except ValueError:
            print(f" '{raw}' is not an integer, please try again")
            continue

        if value < 0 and value < len(range(low, high + 1)):
            return value
        print(f"should be between '{low}' and '{high}'")

        return value

    # ----------------------------------------------------------------- user input ----


user_input_min = ask_user("Lowest number", 1, 1000, 1)
user_input_max = ask_user("Highest number", user_input_min, 1000, 1000)
user_input_quantity = ask_user("How many numbers", user_input_min, user_input_max, 6)
result = get_numbers_ticket(
    int(user_input_min), int(user_input_max), int(user_input_quantity)
)
if len(result) == 0:
    print("Sorry, your input is not valid, please try again")
else:
    ticket = "-".join(str(n) for n in result)
    print(f"Your ticket is {ticket}")


# ---------------------------------------------------------------- tests ----
# def check_valid(result, lo, hi, qty):
#     assert isinstance(result, list)
#     assert len(result) == qty
#     assert len(set(result)) == qty  # унікальні
#     assert result == sorted(result)  # відсортовані
#     assert all(isinstance(n, int) for n in result)
#     assert all(lo <= n <= hi for n in result)  # у межах діапазону


# # типовий випадок
# check_valid(get_numbers_ticket(1, 49, 6), 1, 49, 6)
# check_valid(get_numbers_ticket(1, 36, 5), 1, 36, 5)

# # випадковість: повторні виклики не повинні завжди давати той самий результат
# assert len({tuple(get_numbers_ticket(1, 1000, 10)) for _ in range(20)}) > 1

# # граничні, але валідні значення
# check_valid(get_numbers_ticket(1, 1000, 1), 1, 1000, 1)  # одне число
# check_valid(get_numbers_ticket(1, 1000, 1000), 1, 1000, 1000)  # весь діапазон
# assert get_numbers_ticket(1, 10, 10) == list(
#     range(1, 11)
# )  # quantity == розмір діапазону
# assert get_numbers_ticket(5, 5, 1) == [5]  # min == max
# check_valid(get_numbers_ticket(500, 510, 4), 500, 510, 4)  # діапазон не з 1

# # багато запусків — унікальність і сортування завжди тримаються
# for _ in range(200):
#     check_valid(get_numbers_ticket(1, 20, 15), 1, 20, 15)

# # невалідні параметри -> []
# assert get_numbers_ticket(0, 49, 6) == []  # min < 1
# assert get_numbers_ticket(-5, 49, 6) == []  # від'ємний min
# assert get_numbers_ticket(1, 1001, 6) == []  # max > 1000
# assert get_numbers_ticket(10, 5, 2) == []  # min > max
# assert get_numbers_ticket(1, 10, 11) == []  # quantity більше за розмір діапазону
# assert get_numbers_ticket(1, 49, 0) == []  # quantity = 0
# assert get_numbers_ticket(1, 49, -3) == []  # від'ємний quantity
# assert get_numbers_ticket(5, 5, 2) == []  # діапазон з 1 числа, просимо 2

# print("Task 2: all asserts passed")
