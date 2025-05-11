# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
string = input("enter your text with word with b")
string1 = string.split(" ")
i = 0
for el in string1:
    if el[i] == "b":
        print(string1[i])
        i += 1
    else:
        print("Word with b doesn't exist")

