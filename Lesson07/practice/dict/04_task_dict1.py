items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

#Выведите нумерированый список всех товаров
for item in items:
    print(item["name"])

# 2. Выведите цену самого дешевого товара
price_min = float(items[0]["price"])
for item in items:
    if float(item[price]) < price_min:
        price_min = float(itemp[price])
print(price_min)