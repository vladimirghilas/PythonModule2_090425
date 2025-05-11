a = int(input("введите целое число a "))
b = int(input("введите целое число b "))
k = 0
divider_sum = 0
while a <= b:
    i = 1
    while i < a:
        if a % i == 0:
            divider_sum = divider_sum + i
        i += 1
    if divider_sum == a:
        k += 1
        print(divider_sum)
    divider_sum = 0
    a += 1
print(k)
