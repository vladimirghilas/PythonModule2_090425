# Напишите функцию для расчета площади прямоугольника.
#
# Входные данные:
#   w: ширина прямоугольника.
#   h: высота прямоугольника.
# Результат:
#   площадь прямоугольника.

def calculate_rectangle_area(width, height):
    return width * height


width = int(input("width = "))
height = int(input("height = "))

area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника = {area}")
