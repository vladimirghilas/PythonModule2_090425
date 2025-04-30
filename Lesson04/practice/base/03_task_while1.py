n = int(input("n:"))
i = 0
sum = 0
while i <= n:
    if i%2 == 0:
        sum = sum +i
    i +=1
print("Сумма четных чисел от 0 до",n,"=",sum)