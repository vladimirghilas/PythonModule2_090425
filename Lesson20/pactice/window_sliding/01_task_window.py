# Дан список целых чисел и число k.
# Найти максимальную сумму последовательных элементов списка длины k.
list_ = [4,2,17,3,0,5,20,11,4]
max_sum = 0
k = int(input("enter k"))
for i in range(len(list_)-k+1):
    if max_sum < sum(list_[i:i+k]):
        max_sum = sum(list_[i:i+k])

print(max_sum)