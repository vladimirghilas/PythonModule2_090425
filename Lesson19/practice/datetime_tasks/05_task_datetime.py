# Напишите функцию is_leap_year(year), которая принимает целое число, представляющее год,
# и возвращает True, если год является високосным, и False в противном случае.
# (Напоминание: високосный год делится на 4, кроме годов, делящихся на 100, но не на 400).

def is_leap_year(year: int) -> bool:
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

# Пример использования
year1 = 2024
year2 = 2100
print(f"{year1} - високосный год: {is_leap_year(year1)}")
print(f"{year2} - високосный год: {is_leap_year(year2)}")

# TODO: напишите тесты для функции, используя оператор assert
assert is_leap_year(2020) == True      # divizibil cu 4, nu cu 100
assert is_leap_year(2000) == True      # divizibil cu 400
assert is_leap_year(1600) == True      # divizibil cu 400
assert is_leap_year(1996) == True      # divizibil cu 4, nu cu 100
assert is_leap_year(2400) == True      # divizibil cu 400

# Nu sunt bisecți
assert is_leap_year(2023) == False     # nu e divizibil cu 4
assert is_leap_year(1900) == False     # divizibil cu 100, dar nu cu 400
assert is_leap_year(2100) == False     # divizibil cu 100, dar nu cu 400
assert is_leap_year(2021) == False     # nu e divizibil cu 4
assert is_leap_year(1800) == False     # divizibil cu 100, dar nu cu 400