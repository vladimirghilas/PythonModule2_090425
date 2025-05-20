def display_menu():
    """Отображает меню."""
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить товар.")
    print("5. Найти товар по названию.")
    print("6. Вывести товары с ценой ниже заданной.")
    print("7. Вывести товары с количеством ниже заданного.")
    print("8. Показать статистику инвентаря.")
    print("9. Показать товары с нулевым количеством.")
    print("10. Увеличить количество товара.")
    print("11. Уменьшить количество товара.")
    print("12. Выход. \n")


def show_items(items: list[dict]):
    for i, item in enumerate(items):
        print(f"{i + 1}. ID: {item['id']}")
        print(f"   Название: {item['name']}")
        print(f"   Цена: {item['price']}")
        print(f"   Количество: {item['quantity']}")


def add_item_to_inventory(items: list[dict]) -> None:
    """Добавляет товар в инвентарь"""
    global next_id
    name = input("Введите название товара: ")
    if not name.strip():
        print("Ошибка: Название товара не может быть пустым.")
        return
    for item in items:
        if item["name"].lower() == name.lower():
            print("Ошибка: Товар с таким названием уже существует.")
            return
    while True:
        try:
            price = float(input("Введите цену товара: "))
            if price <= 0:
                print("Ошибка: Цена должна быть положительным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите корректное число для цены.")
    while True:
        try:
            quantity = int(input("Введите количество товара: "))
            if quantity < 0:
                print("Ошибка: Количество  должно быть положительным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите корректное число для количества товара.")

    new_item = {
        "id": next_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    items.append(new_item)
    print(f"Товар '{name}' успешно добавлен id {next_id}.")
    next_id += 1

def remove_item(items: list[dict]):
    try:
        item_id = int(input("Введите id товара для удаления: ").strip())
    except ValueError:
        print("Ошибка: введите корректное число.")
        return

    for i, item in enumerate(items):
        if item["id"] == item_id:
            del items[i]
            print(f"Товар  с id {item_id} успешно удален")
            return
    print(f"Товар с id '{item_id}' не найден.")


def update_item(items: list[dict]):
    try:
        item_id = int(input("Введите id товара : ").strip())
    except ValueError:
        print("Ошибка: введите корректное число.")
        return

    for item in items:
        if item["id"] == item_id:
            try:
                choice = int(input("Введите номер опции для обновления 1. Название 2. Цена 3. Количество: "))
            except ValueError:
                print("Ошибка: введите корректное число.")
                return

            if choice == 1:
                try:
                    name = input("Введите новое название товара: ")
                    if not name.strip():
                        print("Ошибка: Название товара не может быть пустым.")
                        return
                    for other in items:
                        if other["name"].lower() == name.lower() and other["id"] != item_id:
                            print("Ошибка: Товар с таким названием уже существует.")
                            return
                    item['name'] = name
                except ValueError:
                    print("Ошибка: введите корректное число.")
                    return

            elif choice == 2:
                while True:
                    try:
                        price = float(input("Введите новую цену: "))
                        if price <= 0:
                            print("Ошибка: Цена должна быть положительным числом.")
                        else:
                            item["price"] = price
                            print(f"Цена товара '{item['name']}' успешно обновлена.")
                            break
                    except ValueError:
                        print("Ошибка: Введите корректное число для цены.")

            elif choice == 3:
                while True:
                    try:
                        quantity = int(input("Введите новое количество: "))
                        if quantity <= 0:
                            print("Ошибка: Количество должно быть положительным числом.")
                        else:
                            item["quantity"] = quantity
                            print(f" Количество товара '{item['name']}' успешно обновлено.")
                            break
                    except ValueError:
                        print("Ошибка: Введите корректное число для товара.")
            else:
                print("Неверный выбор. Обновление отменено.")
                return
            return
    else:
        print(f"Товар с id '{item_id}' не найден.")

def search_item(items: list[dict]):
    search_str = input("Введите часть названия товара для поиска: ").strip().lower()
    found_items = [item for item in items if search_str in item["name"].lower()]
    if found_items:
        print("Найденные товары:")
        for item in found_items:
            print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
    else:
        print("Товары не найдены.")

def display_below_price(items: list[dict]):
    try:
        price_limit = float(input("Введите максимальную цену: "))
        below_price = [item for item in items if item["price"] < price_limit]
        if below_price:
            print(f"Товары с ценой ниже {price_limit}:")
            for item in below_price:
                print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
        else:
            print(f"Нет товаров с ценой ниже {price_limit}")
    except ValueError:
        print("Ошибка: Введите число.")


def display_below_quantity(items: list[dict]):
    try:
        quantity_limit = int(input("Введите максимальное количество: "))
        below_quantity = [item for item in items if item["quantity"] < quantity_limit]
        if below_quantity:
            print(f"Товары с количеством ниже {quantity_limit}:")
            for item in below_quantity:
                print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
        else:
            print(f"Нет товаров с количеством ниже {quantity_limit}")
    except ValueError:
        print("Ошибка: Введите корректное число для количества.")

def show_inventory_stat(items: list[dict]):
    total_items = len(items)
    total_quantity = sum(item["quantity"] for item in items)
    if total_items > 0:
        average_price = sum(item["price"] for item in items) / total_items
    else:
        average_price = 0
    if items:
        max_price = max(item["price"] for item in items)
        min_price = min(item["price"] for item in items)
    else:
        max_price = 0
        min_price = 0

    print(f"Количество товаров: {total_items}")
    print(f"Общее количество единиц товаров: {total_quantity}")
    print(f"Средняя цена товара: {average_price:.2f}")
    print(f"Самый дорогой товар стоит: {max_price}")
    print(f"Самый дешевый товар стоит: {min_price}")


def show_quantity_zero(items: list[dict]):
    no_products = [item for item in items if item['quantity'] == 0]
    if no_products:
        print("Нет товара для следующих продуктов:")
        for product in no_products:
            print(f"ID: {product['id']}, Название: {product['name']}")
    else:
        print("Все продукты есть в наличии.")


def increase_product_quantity(items: list[dict]):
    try:
        id_raise = int(input("Введите id товара для увеличения "))
        quantity_raise = int(input("Введите количество товара для увеличения "))
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")
        return

    for item in items:
        if item["id"] == id_raise:
            item["quantity"] += quantity_raise
            print(f"Количество товара с id {id_raise} увеличено на {quantity_raise}.")
            break
    else:
        print(f"Товар с id {id_raise} не найден.")


def decrease_product_quantity(items: list[dict]):
    try:
        id_decrease = int(input("Введите id товара для уменьшения "))
        quantity_decrease = int(input("Введите количество товара для уменьшения "))
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")
        return

    for item in items:
        if item["id"] == id_decrease:
            if quantity_decrease < 1:
                print("Ошибка: количество должно быть положительным числом.")
                return
            if item["quantity"] < quantity_decrease:
                print(f"Ошибка: недостаточно товара на складе. Доступно: {item['quantity']}")
                return
            item["quantity"] -= quantity_decrease
            print(f"Количество товара с id {id_decrease} уменьшено на {quantity_decrease}.")
            return
    print(f"Товар с id {id_decrease} не найден.")


inventory = [
    {"id": 1, "name": "Ноутбук", "price": 1200, "quantity": 10},
    {"id": 2, "name": "Мышь", "price": 25, "quantity": 50},
    {"id": 3, "name": "Клавиатура", "price": 50, "quantity": 30},
]
next_id = 4  # глобальный счётчик ID


# Menu
def main():
    menu = {
        '1': show_items,
        '2': add_item_to_inventory,
        '3': remove_item,
        '4': update_item,
        '5': search_item,
        '6': display_below_price,
        '7': display_below_quantity,
        '8': show_inventory_stat,
        '9': show_quantity_zero,
        '10': increase_product_quantity,
        '11': decrease_product_quantity,
    }
    while True:
        display_menu()
        choice = input("Выберите действие (1-12): ").strip()

        if choice == '12':
            print("Завершение работы программы.")
            break
        elif choice in menu:
            try:
                menu[choice](inventory)
            except Exception as e:
                print(f"Произошла ошибка при выполнении операции: {e}")
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 12.")


if __name__ == "__main__":
    main()

#Vladimir Ghilas
