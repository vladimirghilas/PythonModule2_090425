cost = int(input("enter cost: "))
n = int(input("enter quantity "))
i = 1
cost1 = 0
while i <= n:
    cost1 = cost1 + cost
    print(f'{i}{cost1} рублей')
    i += 1
