# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
import random

n = int(input("enter N "))


def gen_rand_num(n, start=1, end=1000):
    return [random.randint(start, end) for _ in range(n)]


list_ = gen_rand_num(n)
list_.sort()
i = 0
for i in range(1, n):
    first = list_[:n - i]
    second = list_[n - i:]
    sum_first = sum(first)
    sum_second = sum(second)
    if sum_first <= 2 * sum_second and sum_second <= 2 * sum_first:
        break
else:
    print("не подходящий список для задания")
print(f'first part: {first}')
print(f'second part: {second}')
print(f'summa first {sum_first}')
print(f'summa second {sum_second}')

#Vladimir Ghilas
