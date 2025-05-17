# "Удвоенные нечетные числа из списка"
# Генераторное выражение, возвращающее удвоенное значение каждого нечетного числа из заданного списка чисел.
<<<<<<< HEAD
list = [2,4,5,8,-1,-3,7,9,11]
result = (el * 2 for el in list if el % 2 !=0)
for num in result:
    print(num)
# def odd_two(list):
#     for el in list:
#         if int(list[el]) % 2 != 0:
#             yield list[el] * 2
#
#
# for num in odd_two([2, 3, 4, 5, 6, 7, 8, 9, 10]):
#     print(num)
=======

data = [2, 4, -5, 10, 8, 3]

result =(number * 2 for number in data if number % 2 != 0)
print(list(result))
>>>>>>> cfc7a9b39710a1b574d089247f0f41f4336dc744
