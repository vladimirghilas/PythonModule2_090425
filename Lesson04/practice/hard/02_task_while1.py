n = int(input("введите длину стороны квадрата 1 < n < 20 "))
i = 0
while i < n:
    j = 0
    while j < n:
        if i == j or i + j == n - 1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1
