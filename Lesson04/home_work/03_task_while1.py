n = int(input("enter natural number 1..9 "))
i = 1
while i <= n:
    k = 1
    while k <= n:
        print(k*i,  end= "\t ")
        k += 1
    print()
    i +=1
