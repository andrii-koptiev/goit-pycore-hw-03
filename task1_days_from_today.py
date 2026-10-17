"""
Завдання 1. get_days_from_today(date)

Створіть функцію get_days_from_today(date), яка розраховує кількість днів
між заданою датою і поточною датою.

Вимоги:
- Параметр date — рядок у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
- Повертає ціле число — кількість днів від заданої дати до поточної.
  Якщо задана дата пізніша за поточну, результат від'ємний.
- Враховуються лише дні, час (години, хвилини, секунди) ігнорується.
- Використовуйте модуль datetime.
- Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.

Підказки:
- datetime.strptime(date, "%Y-%m-%d")
- datetime.today()
- різниця (today - given).days

Приклад: якщо сьогодні 2021-05-05, get_days_from_today("2021-10-09") == -157
"""

from datetime import date, datetime, timedelta


def get_days_from_today(date: str) -> int | None:
    try:
        validated_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()

        return (today - validated_date).days
    except ValueError:
        print("Input is empty or wrong format")
        return None


# ---------------------------------------------------------------- tests ----
today = datetime.today().date()


def format_date(value: date) -> str:
    return value.strftime("%Y-%m-%d")


# сьогодні -> 0
assert get_days_from_today(format_date(today)) == 0

# минулі дати -> додатні
assert get_days_from_today(format_date(today - timedelta(days=1))) == 1
assert get_days_from_today(format_date(today - timedelta(days=30))) == 30
assert get_days_from_today(format_date(today - timedelta(days=365))) == 365

# майбутні дати -> від'ємні
assert get_days_from_today(format_date(today + timedelta(days=1))) == -1
assert get_days_from_today(format_date(today + timedelta(days=157))) == -157

# фіксована дата у минулому, звіряємо з ручним розрахунком
assert get_days_from_today("2020-10-09") == (today - datetime(2020, 10, 9).date()).days

# результат — саме int
assert isinstance(get_days_from_today(format_date(today)), int)

# високосний день існує
assert get_days_from_today("2024-02-29") == (today - datetime(2024, 2, 29).date()).days

# невалідні формати -> None (не повинно падати з винятком)
assert get_days_from_today("2021/10/09") is None  # інші роздільники
assert get_days_from_today("09-10-2021") is None  # інший порядок
assert get_days_from_today("2021-13-01") is None  # неіснуючий місяць
assert get_days_from_today("2021-02-30") is None  # неіснуючий день
assert get_days_from_today("2023-02-29") is None  # не високосний рік
assert get_days_from_today("") is None  # порожній рядок
assert get_days_from_today("not a date") is None  # сміття
assert get_days_from_today("20211009") is None  # число замість рядка

print("Task 1: all asserts passed")


# ----------------------------------------------------------------- main ----
if __name__ == "__main__":
    user_input = input("Enter a date in ISO format (YYYY-MM-DD): ").strip()
    get_days_from_today(user_input)
