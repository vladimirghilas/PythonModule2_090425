a = int(input("enter a "))
b = int(input("enter b "))
c = int(input("enter c "))

if a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        print("Равнобедренны")
    else:
        print("Не равнобедренный")
else:
    print("Не существует")
