path = "data/numbers.txt"
sum_number = 0
count = 0
f = open(path, "r")
for line in f:
    sum_number += int(line)
    count +=1
f.close()
print(sum_number)
print(sum_number/count)
