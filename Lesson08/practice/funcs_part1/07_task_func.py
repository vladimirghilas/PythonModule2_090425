# Напишите функцию принимающую время в секундах и возвращающую
# строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def format_seconds(sec):
    hours = sec // 3600
    seconds = sec % 60
    minutes = (sec // 60) % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'


sec = int(input("enter seconds "))
print(format_seconds(sec))
