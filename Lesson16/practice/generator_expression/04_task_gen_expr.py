# "Буквы верхнего регистра из строки"
# Генераторное выражение, возвращающее все буквы верхнего регистра из заданной строки.
string ="Hello World"
result = (char for char in string.upper() )
for el in string:
    print(next(result))
