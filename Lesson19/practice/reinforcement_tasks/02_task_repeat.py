# "Генератор слов из строки"
#
# Входные данные: Строка text.
# Результат: Генератор, выдающий по одному слову из входной строки.

def words_from_string(text: str):
    text1 = text.split()
    for el in text1:
        yield el

# Пример использования:
for word in words_from_string("Это пример строки для генератора"):
    print(word)
