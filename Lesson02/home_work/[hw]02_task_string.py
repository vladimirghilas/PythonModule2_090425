# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
<<<<<<< HEAD
<<<<<<< HEAD
string = input("enter your text with word with b")
string1 = string.split(" ")
i = 0
for el in string1:
    if el[i] == "b":
        print(string1[i])
        i += 1
    else:
        print("Word with b doesn't exist")

=======
=======
>>>>>>> patch3
string = input('введите строку ')
s = string.find('b')
sp = string.find(" ",s)
word = string [s:sp]
print(word)
<<<<<<< HEAD
>>>>>>> patch-1
=======
>>>>>>> patch3
