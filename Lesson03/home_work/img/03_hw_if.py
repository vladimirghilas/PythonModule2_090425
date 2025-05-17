x1 = int(input("enter first x num 1..8 "))
y1 = int(input("enter first y num 1..8 "))
x2 = int(input("enter second x num 1..8 "))
y2 = int(input("enter second y num 1..8 "))

if (x1+y1)%2 == 0 and (x2+y2)%2 == 0 or(x1+y1)%2 != 0 and (x2+y2)%2 != 0:
    print("Yes")
else:
    print("No")