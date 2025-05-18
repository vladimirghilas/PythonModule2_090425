def validate_arguments(funct):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Все аргументы должны быть > 0")
        return funct(*args, **kwargs)
    return wrapper

@validate_arguments
def multipay(a,b):
    return a*b

print(multipay(5,6))
print(multipay(-5,6))