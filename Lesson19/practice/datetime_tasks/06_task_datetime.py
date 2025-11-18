# "Вычисление возраста"

# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.
from datetime import datetime, date
def birthday_parce(birthday_str):
    try:
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
        return birthday
    except:
        print("Неверный формат даты. Используйте формат YYYY-MM-DD.")
        return None

def calculate_age(birthday) -> int:
    today = date.today()
    age = today.year - birthday.year
    if (today.month, today.day) <(birthday.month, birthday.day):
        age -= 1
    return age

def is_birthday_today(birthday):
    today = date.today()
    return (today.month, today.day) == (birthday.month, birthday.day)

user_input = input("Введите дату рождения (в формате YYYY-MM-DD): ")
birthdate = birthday_parce(user_input)
if birthdate:
    age = calculate_age(birthdate)
    print(f'your birthday is {birthdate} your are {age} old')

    if is_birthday_today(birthdate):
        print("С днём рождения!")
    else:
        print("Сегодня не ваш день рождения.")

#1. Testare parsare dată validă
assert birthday_parce("2000-05-20") == date(2000, 5, 20)

# 2. Testare parsare dată invalidă (va returna None)
assert birthday_parce("20-05-2000") is None

# 3. Testare vârstă (dacă azi e 2025-05-20)
assert calculate_age(date(2000, 5, 20)) == 25

# 4. Testare vârstă când ziua și luna nu au venit încă (2025-05-20 azi, ziua pe 21)
assert calculate_age(date(2000, 5, 21)) == 24

# 5. Testare dacă azi e ziua de naștere (2025-05-20 azi)
assert is_birthday_today(date(2000, 5, 20)) == True