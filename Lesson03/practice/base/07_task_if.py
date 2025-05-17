a = int(input("enter first size"))
b = int(input("enter second size"))
c = int(input("enter third size"))
if a + b > c and a + c > b and b + c > a:
    if a==b or a==c or b==c:
        print("isosceles triangle")
    else:
        print("triangle isn't isosceles")
else:
    print("triangle don't exists")