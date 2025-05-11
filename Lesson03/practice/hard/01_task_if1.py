n = int(input("enter number 4 digits"))
n1 = n//10
n2 = n%10*10
n3 = n2 + n1%10
if n // 100 == n3:
    print("Yes")
else:
    print('No')