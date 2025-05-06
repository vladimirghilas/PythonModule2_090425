# "Работа со списком товаров"
#
# Создайте список словарей, представляющих несколько товаров (минимум 4 товара).
# Выведите на экран нумерованный список всех названий товаров
items = [
    {"name": "paints", "price": 35, "quantity": 10},
    {"name": "hat", "price": 5, "quantity": 8},
    {"name": "shoes", "price": 8, "quantity": 100},
    {"name": "shirt", "price": 23, "quantity": 16}
]
for i, item in enumerate(items, 1):
    print(f'{i} {item["name"]}')
