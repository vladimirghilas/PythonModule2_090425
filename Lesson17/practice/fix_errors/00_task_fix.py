# Даны функции
def average(numbers: list) -> float:
    "Нахождение среднеарифметического"
    total = sum(numbers)
    return total / len(numbers)


def get_unique_elements(data: list) -> list:
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)
        else:
            unique.append(item)
    return unique
if __name__ in "__main__":
    assert average([3,3,3,]) == 3
    assert average([0, 2, 0, 2]) == 1
    assert average([10]) == 5
    assert average([5, -5, 6]) == 2
assert get_unique_elements([2, 4, 2, 4, 0]) ==[2, 4, 0]
assert get_unique_elements([2, 4, -2, -2, 6, 6, 6]) == [2, 4, -2, 6]
assert get_unique_elements([3,3,3,]) == 3
assert get_unique_elements([3,3,3,]) == 3
# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
