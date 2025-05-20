# "Вычисление возраста"

# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

from datetime import date, datetime, timedelta

# TODO: напишите тесты для функции, используя оператор assert

def get_age(birthday_str: str) -> int:
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    today = datetime.now()
    delta_date = today - birthday
    return delta_date.days // 365

print(get_age("2000-01-10")) # 25
print(get_age("2000-05-20")) # 25
print(get_age("2000-05-19")) # 25
print(get_age("2000-05-21")) # 24