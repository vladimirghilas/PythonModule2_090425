# "Получение завтрашней даты"
#
# Напишите функцию get_tomorrow_date(), которая возвращает объект date,
# представляющий завтрашнюю дату относительно текущей даты.

from datetime import date, timedelta


def get_tomorrow_date(today: date) -> date:
    tomorow_date = today + timedelta(days=1)
    return tomorow_date


print(get_tomorrow_date(date(2025, 5, 16)))
# TODO: напишите тесты для функции, используя оператор assert
assert get_tomorrow_date(date(2025, 5, 16)) == date(2025, 5, 17)
assert get_tomorrow_date(date(2024, 2, 28)) == date(2024, 2, 29)  # an bisect
assert get_tomorrow_date(date(2024, 2, 29)) == date(2024, 3, 1)   # final de februarie bisect
assert get_tomorrow_date(date(2025, 12, 31)) == date(2026, 1, 1)  # trecere de an
assert get_tomorrow_date(date(2025, 4, 30)) == date(2025, 5, 1)   # lună cu 30 zile


