# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")
item1 = []
for item in items:
    if item["brand"] not in item1:
        item1.append(item["brand"])
print(*item1, sep=", ")

print("На складе больше всего товаров брэнда(ов): ")

more_brands = {}
for item in items:
    brand = item["brand"]
    if brand in more_brands:
        more_brands[brand] += 1
    else:
        more_brands[brand] = 1
for brand in more_brands:
    if more_brands[brand] > 1:
        print(more_brands[brand], brand)

print("На складе самый дорогой товар брэнда(ов): ")

hight_price = {}
price = 0
for item in items:
    if item["price"] > price:
        price = item["price"]
        hight_price = item
print(hight_price["brand"])