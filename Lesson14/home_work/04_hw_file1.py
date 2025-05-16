path = "data/fruits.txt"
d = list(map(chr,range(ord("А"),ord("Я")+1)))
with open(path, "r", encoding="UTF-8") as f:
    for line in f:
        if line[0] in d:
            path1 = "data/"+"fruits_" + line[0] + ".txt"
            with open(path1,"a", encoding="UTF-8") as file:
                file.write(line)
