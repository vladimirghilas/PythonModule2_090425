def check_age(age):
    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.
    return age
age = int(input("enter age  "))

while True:
    if age < 0:
        print("enter age > 0")

    break

print(check_age(age))