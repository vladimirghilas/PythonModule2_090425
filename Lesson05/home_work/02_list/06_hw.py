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
        "price": 2700
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
<<<<<<< HEAD
item_brand = []
for item in items:
    if item["brand"] not in item_brand:
        item_brand.append(item["brand"])
print(item_brand)
=======
item1 = []
for item in items:
    if item["brand"] not in item1:
        item1.append(item["brand"])
print(*item1, sep=", ")
>>>>>>> patch3

print("На складе больше всего товаров брэнда(ов): ")
counts = {}
for item in items:
    key = item["brand"]
    if key in counts:
        counts[key] += 1
    else:
        counts[key] = 1
for brand, count in counts.items():
    if count >1:
        print(brand, count)



<<<<<<< HEAD

print("На складе самый дорогой товар брэнда(ов): ")

max_price = ''
cost = 0
for item in items:
    if item["price"] > cost:
        cost = item["price"]
        max_price = item["brand"]
    elif item["price"] == cost:
        max_price= max_price +" "+ item['brand']
print(max_price)


=======
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
>>>>>>> patch3
