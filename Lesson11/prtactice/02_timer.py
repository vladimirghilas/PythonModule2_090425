# Напишите декоратор timer, который измеряет время выполнения декорируемой функции и выводит его в консоль.


import time


def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'result is {end - start:.4f} seconds')
        return func
    return wrapper


@timer
def my_function():
    time.sleep(2)
    print("Функция выполнена")


my_function()
