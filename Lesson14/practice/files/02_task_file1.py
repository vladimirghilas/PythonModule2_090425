path_read = "data/limericks.txt"
path_write = ("data/clean_limericks.txt")

file_in = open(path_read,"r", encoding = "UTF-8")
file_out = open(path_write,"w", encoding = "UTF-8")
for line in file_in:
    new_line = line.replace(","," ")
    file_out.write(new_line)

file_in.close()
file_in.close()
