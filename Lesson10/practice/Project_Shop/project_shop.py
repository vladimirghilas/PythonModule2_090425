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
    print("8. Выход. \n")


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
        if item["name"] == name:
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
            if quantity <= 0:
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
    item_id = int(input("Введите id товара для удаления: ").strip())
    for i, item in enumerate(items):
        if item["id"] == item_id:
            del items[i]
            return
    print(f"Товар с id '{item_id}' не найден.")

def update_item(items: list[dict]):
    item_id = int(input("Введите id товара : ").strip())
    for item in items:
        if item["id"] == item_id:
            choice = int(input("Введите номер опции для обновления 1. Название 2. Цена 3. Количество: "))
            if choice == 1:
                name = input("Введите новое название товара: ")
                if not name.strip():
                    print("Ошибка: Название товара не может быть пустым.")
                    return
                for other in items:
                    if other["name"] == name:
                        print("Ошибка: Товар с таким названием уже существует.")
                        return
                item['name'] = name
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
        '7': display_below_quantity
    }
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        if choice == '8':
            print("Завершение работы программы.")
            break
        elif choice in menu:
            menu[choice](inventory)
        else:
            print("Некорректный ввод. Пожалуйста, выберите операцию из меню.")

if __name__ == "__main__":
    main()