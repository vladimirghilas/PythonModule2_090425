n = int(input("введите целое число "))
i = 1
divider_sum = 0
while i < n:
    if n % i == 0:
        divider_sum = divider_sum + i
    i += 1
if divider_sum == n:
    print("да")
else:
    print("нет")
