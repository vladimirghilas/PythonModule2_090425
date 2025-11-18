# "Сортировка списка строк по количеству гласных букв"
#
# Описание: Дан список строк.
# Необходимо отсортировать этот список по количеству гласных букв латинского алфавита в каждой строке.

strings = ["hello", "world", "programming", "python", "ai"]
vowels = "aeyiou"
count = 0
lt = []
for el in strings:
    for i in el:
        if i.lower() in vowels:
            count +=1
    lt.append((count,el))
    count = 0
print(sorted(lt))