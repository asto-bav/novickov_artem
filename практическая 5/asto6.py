import math


def calculate_distance(x1, y1, x2, y2):
    """Вычисляет расстояние между двумя точками."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calculate_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


x1, y1 = map(float, input("Введите координаты точки A: ")
x2, y2 = map(float, input("Введите координаты точки B: ")
x3, y3 = map(float, input("Введите координаты точки C: ")

a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x2, y2, x3, y3)
c = calculate_distance(x3, y3, x1, y1)

area = calculate_triangle_area(a, b, c)

print(f"Площадь треугольника: {area:.2f}")