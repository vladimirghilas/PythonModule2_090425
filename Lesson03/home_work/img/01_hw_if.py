n = int(input("enter first size"))
m = int(input("enter second size"))
k = int(input("enter third size"))

if n<=k<n*m and (k%n==0 or k%m==0):
    print("Yes")
else:
    print("No")
