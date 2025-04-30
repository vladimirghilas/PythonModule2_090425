n = int(input("n:"))
i = 2
is_prime = True
while i < n:
    if n%i == 0:
        is_prime = False
        print(f'have divisor {i}')
    i += 1
if is_prime:
    print("simple number")
