# Задача: добавьте обработку пользовательского ввода.
# Если будет введено некорректное значение, выведите сообщение об этом.
# При корректном значении, вычислите значение выражения и выведите результат.

<<<<<<< HEAD
=======

>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
<<<<<<< HEAD
        print("enter another number")

result = number ** 2 - 4 * number
print(result)
=======
        print("Некорректное значение")

result = number ** 2 - 4 * number
print(result)
>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
