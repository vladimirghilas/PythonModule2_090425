# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов этих чисел.
def square(number):
    return number ** 2

def sum_of_squares(numbers):
    return sum(map(square, numbers))

print(sum_of_squares([2, -4, 5]))