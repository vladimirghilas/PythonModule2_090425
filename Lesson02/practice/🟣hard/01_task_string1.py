from itertools import count

string = input("enter your text")
i = 0
count = 0
string1 = string.split(" ")
for el in string1:
    if len(string1[i]) > 5:
        count +=1
    i +=1
print(count)