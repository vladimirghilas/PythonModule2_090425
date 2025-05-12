n = int(input("n:"))
i = 0
positive_number = 0
while i <=n:
    num = int(input("enter number"))
    if num > 0:
        positive_number +=1
    i += 1
print("was entered",positive_number,"positive number")