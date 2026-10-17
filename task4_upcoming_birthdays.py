"""
Завдання 4. get_upcoming_birthdays(users)

Визначає, кого з колег потрібно привітати з днем народження протягом
наступних 7 днів включно з поточним днем.

Вимоги:
- users — список словників: {"name": str, "birthday": "рік.місяць.дата"},
  напр. {"name": "John Doe", "birthday": "1985.01.23"}.
- Потрібні ті, чий день народження (місяць+день) припадає на діапазон
  [сьогодні, сьогодні + 7 днів] (різниця 0..7 днів включно).
  Якщо день народження в цьому році вже минув — розглядайте наступний рік.
- Якщо день народження випадає на суботу чи неділю, дату привітання
  переносимо на наступний понеділок (перенесена дата може вийти
  за межі 7 днів — користувача все одно включаємо).
- Повертає список словників:
  {"name": str, "congratulation_date": "рік.місяць.дата"}
  (рік — той, в якому відбудеться привітання).

Підказки:
- datetime.strptime(user["birthday"], "%Y.%m.%d").date()
- datetime.today().date()
- date.replace(year=...), date.weekday() (5 = субота, 6 = неділя)

Приклад: сьогодні 2024.01.22, users:
  John Doe 1985.01.23, Jane Smith 1990.01.27 ->
  [{'name': 'John Doe', 'congratulation_date': '2024.01.23'},
   {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}]  # 27-го субота

Увага: тести нижче залежать від поточної дати і будуються відносно неї.
Вікно 0..7 днів завжди містить вихідні, тож обидва сценарії покриті.
"""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # TODO: ваша реалізація
    pass


# ---------------------------------------------------------------- tests ----
today = datetime.today().date()


def birthday_str(target, year=2000):
    """Рядок дня народження, що припадає на дату target (рік 2000 — високосний)."""
    return f"{year}.{target.month:02d}.{target.day:02d}"


def expected_congrats(target):
    """Очікувана дата привітання: вихідні -> наступний понеділок."""
    if target.weekday() == 5:
        target += timedelta(days=2)
    elif target.weekday() == 6:
        target += timedelta(days=1)
    return target.strftime("%Y.%m.%d")


# кожен зсув 0..7 днів -> користувач у результаті, з правильною датою
for offset in range(0, 8):
    target = today + timedelta(days=offset)
    users = [{"name": f"User{offset}", "birthday": birthday_str(target)}]
    assert get_upcoming_birthdays(users) == [
        {"name": f"User{offset}", "congratulation_date": expected_congrats(target)}
    ], f"offset={offset}"

# поза вікном: вчора і через 8+ днів -> не включаються
for offset in (-1, -7, 8, 9, 30, 180):
    target = today + timedelta(days=offset)
    users = [{"name": "Out", "birthday": birthday_str(target)}]
    assert get_upcoming_birthdays(users) == [], f"offset={offset}"

# порожній список
assert get_upcoming_birthdays([]) == []

# день народження сьогодні (різні роки народження не впливають)
for year in (1950, 1999, 2000, 2020):
    users = [{"name": "Today", "birthday": birthday_str(today, year)}]
    res = get_upcoming_birthdays(users)
    assert res == [{"name": "Today", "congratulation_date": expected_congrats(today)}]

# змішаний список: потрібні лише ті, хто у вікні, порядок збережено
users = [
    {"name": "Soon", "birthday": birthday_str(today + timedelta(days=2))},
    {"name": "Past", "birthday": birthday_str(today - timedelta(days=3))},
    {"name": "Far", "birthday": birthday_str(today + timedelta(days=40))},
    {"name": "Edge", "birthday": birthday_str(today + timedelta(days=7))},
]
res = get_upcoming_birthdays(users)
assert [r["name"] for r in res] == ["Soon", "Edge"]
assert res[0]["congratulation_date"] == expected_congrats(today + timedelta(days=2))
assert res[1]["congratulation_date"] == expected_congrats(today + timedelta(days=7))

# двоє користувачів з однією датою обидва включаються
users = [
    {"name": "A", "birthday": birthday_str(today + timedelta(days=3), 1980)},
    {"name": "B", "birthday": birthday_str(today + timedelta(days=3), 1995)},
]
assert [r["name"] for r in get_upcoming_birthdays(users)] == ["A", "B"]

# формат результату: ключі, рядок дати 'рік.місяць.дата', дата не раніше сьогодні
for r in get_upcoming_birthdays(
    [{"name": "F", "birthday": birthday_str(today + timedelta(days=1))}]
):
    assert set(r.keys()) == {"name", "congratulation_date"}
    parsed = datetime.strptime(r["congratulation_date"], "%Y.%m.%d").date()
    assert parsed >= today
    assert parsed.weekday() < 5  # привітання ніколи не на вихідний

# вхідний список не мутується
users = [{"name": "X", "birthday": birthday_str(today + timedelta(days=1))}]
snapshot = [dict(u) for u in users]
get_upcoming_birthdays(users)
assert users == snapshot

print("Task 4: all asserts passed")
