n = int(input("enter n "))
path = "data/piramida.txt"

line = " "
with open(path, "w", encoding="UTF-8") as f:
    for i in range(1,n+1):
        line = "*" * (2*i-1)
        print(f"{line:^{2*n-1}}")