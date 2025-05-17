# Дана функция
def count_vowels(text: str) -> int:
    "Подсчет гласных "
    vowels = "eyuioa"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
assert count_vowels("any") == 2
assert count_vowels("") == 0
