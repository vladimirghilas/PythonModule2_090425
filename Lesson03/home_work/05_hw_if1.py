a = int(input("enter number 1 "))
b = int(input("enter number 2 "))
c = int(input("enter nunber 3 "))

if c < b:
    c, b = b, c
if c < a:
    c, a = a, c
if b < a:
    a, b = b, a
print(a,b,c)  #->  "вывели номера в порядке возростания"


