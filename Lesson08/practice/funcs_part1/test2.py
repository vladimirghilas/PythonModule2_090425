from fractions import Fraction

def simplified_number(s):
    f = Fraction(s)
    f = f.limit_denominator()
    whole = f.numerator // f.denominator
    remainder = f - whole

    if remainder == 0:
        return str(whole)
    return f"{whole} {remainder.numerator}/{remainder.denominator}"


print(simplified_number(22 / 7))