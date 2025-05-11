n = int(input("enter number 1..12 "))

if n == 1 or n ==2 or n == 12:
    print("Зима")
elif 2<n<6:
    print("Весна")
elif 5<n<9:
    print('Лето')
else:
    print("Осень")