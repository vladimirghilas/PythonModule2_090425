a = int(input("enter first size"))
b = int(input("enter second size"))
c = int(input("enter third size"))
if a+b>c and a+c>b and b+c>a:
    print("triangle exist")
else:
    print("triangle don't exist")