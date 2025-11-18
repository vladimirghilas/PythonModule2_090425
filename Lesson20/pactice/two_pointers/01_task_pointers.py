# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Гарантируется, что в списке если пара, сумма которых равна target

num = [2, 5, 7, 10]
target = 8
left = 0
right = 3
i = 0
while i < len(num):
    if num[left] + num[right] == target:
        print(target)
        break
    elif left == right:
        print("summa not found")
        break
    elif num[left] + num[right] > target:
        right -= 1
        i +=1
    elif num[left] + num[right] < target:
        left +=1
        i +=1

