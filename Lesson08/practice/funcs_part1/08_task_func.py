# Напишите функцию находящую n-ое число Фибоначчи.
<<<<<<< HEAD
<<<<<<< HEAD

def fibonacci(n):
    ...

fibonacci(6)
fibonacci(8)

# 1 2 3 4 5 6  7 8
# 1 1 2 3 5 8 13 21
=======
def fibanaci(n):
    k = 0
    m = 1
    for i in range(n-2):
        c = k + m
        k = m
        m = c
    return print(f'{m}')

n = int(input("enter n "))
fibanaci(n)
>>>>>>> patch-1
=======
def fibanaci(n):
    k = 0
    m = 1
    for i in range(n-2):
        c = k + m
        k = m
        m = c
    return print(f'{m}')

n = int(input("enter n "))
fibanaci(n)
>>>>>>> patch3
