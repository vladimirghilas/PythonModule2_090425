# Задача: добавьте обработку пользовательского ввода.
# Если будет введено некорректное значение, выведите сообщение об этом.
# При корректном значении, вычислите значение выражения и выведите результат.

while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("enter another number")

result = number ** 2 - 4 * number
print(result)
