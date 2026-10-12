
try:
    column_1 = int(input("Столбец первой клетки: "))
    row_1 = int(input("Строка первой клетки: "))
    column_2 = int(input("Столбец второй клетки: "))
    row_2 = int(input("Строка второй клетки: "))

    if not (1 <= column_1 <= 8 and
            1 <= row_1 <= 8 and
            1 <= column_2 <= 8 and
            1 <= row_2 <= 8):
        print("Ошибка ввода")

    elif (column_1 == column_2 or
          row_1 == row_2 or
          abs(column_1 - column_2) == abs(row_1 - row_2)):
        print("YES")

    else:
        print("NO")

except ValueError:
    print("Ошибка ввода")
