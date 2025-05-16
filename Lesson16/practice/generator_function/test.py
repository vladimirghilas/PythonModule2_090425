# filter positive numbers

def is_positive(numbers):
    print("is_positive")
    return numbers > 0


def is_even(number):
    print("is_even")
    return number % 2 == 0


def my_filter(funct, iterable):
    for el in iterable:
        if funct(el):
            print("my_filter")
            yield el


data = [12, 4, 0, -13, 20, 5, 8, -8, -3, 22]

result = my_filter(is_even, my_filter(is_positive, data))

next(result)

print(result)

def log(func):
    def wrapper(*args, **kwargs):
        print(f"вызвана функция {func.__name__}")
        return func(*args, **kwargs)
        return wrapper