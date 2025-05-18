# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    if len(ticket_number_str) != 6:
        return False
    part1 = ticket_number_str[:3]
    part2 = ticket_number_str[3:]
    sum_part1 = 0
    sum_part2 = 0
    for el in part1:
        sum_part1 += int(el)
    for el in part2:
        sum_part2 += int(el)

    return sum_part1 == sum_part2

def lucky_ticket_v2(ticket_number):
    # ticket_number = 123456
    # ticket_number % 10 -> 6
    # ticket_number // 10 -> 12345
    sum_part1 = 0
    sum_part2 = 0
    num_digit = 6
    while ticket_number != 0:
        digit = ticket_number % 10
        ticket_number = ticket_number // 10
        if num_digit > 3:
            sum_part2 += digit
        else:
            sum_part1 += digit
        num_digit -= 1

    return sum_part1 == sum_part2

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
print(lucky_ticket_v2(123006)) # True
print(lucky_ticket_v2(123206)) # False

print(lucky_ticket_v2(436751)) # True
# print(lucky_ticket(12321))
# print(lucky_ticket(1232123))