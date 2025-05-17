# Дана функция
def remove_duplicates(data):
    "Удаление дубликатов из списка"
    for item in data.copy():
        if data.count(item) > 1:
            data.remove(item)
    return data

# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
assert  remove_duplicates([2, 2, 2]) == [2]
assert  remove_duplicates([]) == []