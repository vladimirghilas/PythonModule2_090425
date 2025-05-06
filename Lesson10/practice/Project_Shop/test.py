def recursion(n):
    if n>=0:
        recursion(n-1)
        print(f'n={n}')

recursion(5)