import math
def calculate_rectangle_area(width, height):
    """Возвращает площадь прямоугольника по ширине и высоте."""
    return width * height
def calculate_circle_area(radius):
    """Возвращает площадь круга по заданному радиусу."""
    return math.pi * radius ** 2
width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))
rectangle_area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника: {rectangle_area:.2f}")
radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)
print("Площадь круга:", circle_area)