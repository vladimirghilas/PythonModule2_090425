import math

x = int(input("enter x0 "))
y = int(input("enter y0 "))
xr = int(input("enter x1 "))
yr = int(input("enter y1 "))
r = int(input("enter r "))

l = math.sqrt((xr - x) ** 2 + (yr - y) ** 2)

if l <= r:
    print("Yes")
else:
    print("No")
