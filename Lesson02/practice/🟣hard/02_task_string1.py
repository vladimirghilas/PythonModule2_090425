s1 = input("enter first text")
s2 = input("enter second text")

i = 0
ok = True
while i < len(s2):
    c = s2[i]
    if c in s1:
        p = s1.index(c)
        s1 = s1[0:p] + s1[p +1:]
        i += 1
    else:
        ok = False
        break
if ok:
    print("Yes")
else:
    print("No")

