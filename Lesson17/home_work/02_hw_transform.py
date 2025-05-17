# У вас есть список строк.
# Вам нужно получить список длин всех строк, которые имеют длину более 3 символов.

lenght_word = []
words = ["cat", "dog", "elephant", "mouse", "bird", "ant"]
for word in words:
    if len(word) > 3:
        lenght_word.append(len(word))
print(lenght_word)

lenght_word = list(map(len, (filter(lambda word:len(word) > 3, words))))
print(lenght_word)