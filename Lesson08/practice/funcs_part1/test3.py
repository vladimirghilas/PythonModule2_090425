from fractions import Fraction
def simplified_number(s):
    f = Fraction(s)
    f = f.limit_denominator()
    whole = f.numerator // f.denominator
    remainder = f - whole
    if whole == 0:
        return whole
    return (f'{whole} {remainder}')
print(simplified_number(4/3))