# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(n):
    string = str(n)
    i = 0
    k = 1
    last2 = 0
    first2 = 0
    while i < len(string):
        i += 1
        k = k * 10
        m = (n % k) // (k / 10)
        if i == 1 or i == 2:
            last2 = last2 + m
        elif i == len(string) - 1 or i == len(string):
            first2 = first2 + m
    return "Счастливый билет" if first2 == last2 else "Обычный билет"

#n = int(input("Введите номер "))
# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))