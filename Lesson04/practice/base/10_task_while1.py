a = int(input("a:"))
b = int(input("b:"))

cant = 0
while a < b:
    i = 1
    sum = 0
    while i < a:
        if a % i == 0:
            sum = sum +i
        i +=1
    if sum == a:
        print(f'result is {a}')
        cant +=1
    a +=1
print(cant)