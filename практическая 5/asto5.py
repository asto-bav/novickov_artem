BANKNOTES = [5000, 2000, 1000, 500, 200, 100]

amount = int(input("Введите сумму для снятия: "))

if amount <= 0 or amount % 100 != 0:
    print("Ошибка! Сумма должна быть положительной и кратной 100.")
else:
    for banknote in BANKNOTES:
        count = amount // banknote
        amount = amount % banknote

        if count > 0:
            print(f"Купюр {banknote} руб.: {count} шт.")

    if amount == 0:
        print("Выдача рассчитана успешно.")