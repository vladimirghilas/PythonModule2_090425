file  = open("data.txt","r", encoding = "UTF-8")

for line in file:
    print(line.rstrip())

file.close()