n = int(input("enter natural number: "))
row  = []
while n != 1:
    if n%2 == 0:
        n = int(n/2)
    else:
        n = 3*n +1
    row.append(n)
print(row)
