# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

from fractions import Fraction

def simplified_number(s):
    f = Fraction(s)
    f = f.limit_denominator()
    whole = f.numerator // f.denominator
    remainder = f - whole
    if whole == 0:
        return whole
    return (f'{whole} {remainder}')


s = input("Введите дроби для сложения или вычитания в формате 5/7+-6/9 \n")
s = s.replace('--', '+').replace('+-', '-').replace('-+', '-')

if '+' in s:
    left, right = s.split('+', 1)
    result = Fraction(left) + Fraction(right)
elif '-' in s[1:]:
    index = s[1:].index('-') + 1
    left, right = s[:index], s[index + 1:]
    result = Fraction(left) + Fraction(right)
else:
    result = s
    Fraction(s)

print(simplified_number(result))
