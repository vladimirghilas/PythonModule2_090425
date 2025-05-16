path = "data/sold.txt"

prices = []

#file = open(path, "r", encoding = "UTF-8")

with open(path, "r") as file:
    for line in file:
        prices += line.split()
print(prices)
prices = list(map(float, prices))
print(sum(prices))
print(max(prices))
print(min(prices))