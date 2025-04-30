n = int(input("n:"))
i = 1
sum = 0
while i < n:
    if n%i == 0:
 #       is_prime = False
 #       print(f'have divisor {i}')
        sum = sum +i
    i += 1
if sum == n:
    print(f'result is yes')
else:
    print(f'result is no')