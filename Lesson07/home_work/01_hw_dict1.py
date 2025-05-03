# Напишите программу,
# которая удаляет элемент из словаря по ключу. Если ключ отсутствует, ничего не делает.

my_dict = {"a": 1, "b": 2, "c": 3}
key = input("Enter key: ")

if key in my_dict:
    del my_dict[key]
    print("key was deleted")
else:
    print("nothing to do")