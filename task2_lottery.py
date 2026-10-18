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

MIN_LIMIT, MAX_LIMIT = 1, 1000


# ---------- rules  ----------
def validate_min_value(min_value: int) -> None:
    if not MIN_LIMIT <= min_value <= MAX_LIMIT:
        raise ValueError(
            f"Lowest number must be {MIN_LIMIT}–{MAX_LIMIT}, got {min_value}."
        )


def validate_max_value(max_value: int, min_value: int) -> None:
    if max_value > MAX_LIMIT:
        raise ValueError(f"Higher '{max_value}' cannot be higher than {MAX_LIMIT}.")

    if min_value > max_value:
        raise ValueError(
            f"Lower '{min_value}' cannot be higher than higher than '{max_value}'."
        )


def validate_quantity(quantity: int, range_length: int) -> None:
    if quantity <= 0:
        raise ValueError(f"Numbers count '{quantity}' must be greater than 0.")

    if quantity > range_length:
        raise ValueError(
            f"Numbers count '{quantity}' cannot be higher than the range length '{range_length}'."
        )


# ---------- implementation  ----------
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not all(type(x) is int for x in (min, max, quantity)):
        return []
    try:
        validate_min_value(min)
        validate_max_value(max, min)
        validate_quantity(quantity, len(range(min, max + 1)))
    except ValueError:
        return []
    else:
        lottery_numbers = random.sample(range(min, max + 1), quantity)
        lottery_numbers.sort()

    return lottery_numbers


# ---------- tests  ----------
def check_valid(result, lo, hi, qty):
    assert isinstance(result, list)
    assert len(result) == qty
    assert len(set(result)) == qty  # унікальні
    assert result == sorted(result)  # відсортовані
    assert all(isinstance(n, int) for n in result)
    assert all(lo <= n <= hi for n in result)  # у межах діапазону


# типовий випадок
check_valid(get_numbers_ticket(1, 49, 6), 1, 49, 6)
check_valid(get_numbers_ticket(1, 36, 5), 1, 36, 5)

# випадковість: повторні виклики не повинні завжди давати той самий результат
assert len({tuple(get_numbers_ticket(1, 1000, 10)) for _ in range(20)}) > 1

# граничні, але валідні значення
check_valid(get_numbers_ticket(1, 1000, 1), 1, 1000, 1)  # одне число
check_valid(get_numbers_ticket(1, 1000, 1000), 1, 1000, 1000)  # весь діапазон
assert get_numbers_ticket(1, 10, 10) == list(
    range(1, 11)
)  # quantity == розмір діапазону
assert get_numbers_ticket(5, 5, 1) == [5]  # min == max
check_valid(get_numbers_ticket(500, 510, 4), 500, 510, 4)  # діапазон не з 1

# багато запусків — унікальність і сортування завжди тримаються
for _ in range(200):
    check_valid(get_numbers_ticket(1, 20, 15), 1, 20, 15)

# невалідні параметри -> []
assert get_numbers_ticket(0, 49, 6) == []  # min < 1
assert get_numbers_ticket(-5, 49, 6) == []  # від'ємний min
assert get_numbers_ticket(1, 1001, 6) == []  # max > 1000
assert get_numbers_ticket(10, 5, 2) == []  # min > max
assert get_numbers_ticket(1, 10, 11) == []  # quantity більше за розмір діапазону
assert get_numbers_ticket(1, 49, 0) == []  # quantity = 0
assert get_numbers_ticket(1, 49, -3) == []  # від'ємний quantity
assert get_numbers_ticket(5, 5, 2) == []  # діапазон з 1 числа, просимо 2
assert get_numbers_ticket(1.5, 49, 6) == []  # type: ignore[arg-type]  # float min
assert get_numbers_ticket(1, 49.0, 6) == []  # type: ignore[arg-type] # float max (навіть "ціле" 49.0)
assert get_numbers_ticket(1, 49, 6.0) == []  # type: ignore[arg-type] # float quantity
assert get_numbers_ticket("1", 49, 6) == []  # type: ignore[arg-type] # рядок замість числа
assert get_numbers_ticket(1, "49", 6) == []  # type: ignore[arg-type]
assert get_numbers_ticket(1, 49, "6") == []  # type: ignore[arg-type]
assert get_numbers_ticket(None, 49, 6) == []  # type: ignore[arg-type] # None
assert get_numbers_ticket(1, None, 6) == []  # type: ignore[arg-type]
assert get_numbers_ticket(1, 49, None) == []  # type: ignore[arg-type]
assert get_numbers_ticket(True, 49, 6) == []  # bool — підклас int, але не число
assert get_numbers_ticket(1, 49, True) == []
assert get_numbers_ticket([1], 49, 6) == []  # type: ignore[arg-type]# список


print("Task 2: all asserts passed")
