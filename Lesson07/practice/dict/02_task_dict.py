# Дана строка.
# Напишите программу, которая подсчитывает частоту каждого символа в строке.

text = "hello world hello python world"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

