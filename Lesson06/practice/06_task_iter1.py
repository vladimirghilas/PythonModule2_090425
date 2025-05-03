word1 = input("enter first word ")
word2 = input("enter second word ")
count = 0
for el in word1:
    if el in word2:
        count+=1
if count == len(word1):
    print("yes")
else:
    print("no")
