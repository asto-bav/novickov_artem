
MIN_NUMBER = 0
MAX_NUMBER = 36

try:
    pocket = int(input("Введите номер кармана: "))

    if not MIN_NUMBER <= pocket <= MAX_NUMBER:
        print("ошибка ввода")

    elif pocket == 0:
        print("зеленый")

    elif 1 <= pocket <= 10:
        if pocket % 2 == 1:
            print("красный")
        else:
            print("черный")

    elif 11 <= pocket <= 18:
        if pocket % 2 == 1:
            print("черный")
        else:
            print("красный")

    elif 19 <= pocket <= 28:
        if pocket % 2 == 1:
            print("красный")
        else:
            print("черный")

    else:
        if pocket % 2 == 1:
            print("черный")
        else:
            print("красный")

except ValueError:
    print("ошибка ввода")