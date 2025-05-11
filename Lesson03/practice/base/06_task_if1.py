a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))

if a + b > c and a + c > b and b + c > a:
    print("exist")
else:
    print("not exist")