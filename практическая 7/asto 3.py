# Цены напитков
COFFEE_PRICE = 120
TEA_PRICE = 80
JUICE_PRICE = 100
WATER_PRICE = 50
LEMONADE_PRICE = 90

print("=" * 45)
print("           ☕ МЕНЮ НАШЕГО КАФЕ")
print("=" * 45)
print("1. Кофе       — 120 руб.")
print("2. Чай        — 80 руб.")
print("3. Сок        — 100 руб.")
print("4. Вода       — 50 руб.")
print("5. Лимонад    — 90 руб.")
print("=" * 45)

choice = input("Выберите напиток (номер или название): ")

match choice:
    case "1" | "Кофе" | "кофе":
        drink = "Кофе ☕"
        price = COFFEE_PRICE
    case "2" | "Чай" | "чай":
        drink = "Чай 🍵"
        price = TEA_PRICE
    case "3" | "Сок" | "сок":
        drink = "Сок 🧃"
        price = JUICE_PRICE
    case "4" | "Вода" | "вода":
        drink = "Вода 💧"
        price = WATER_PRICE
    case "5" | "Лимонад" | "лимонад":
        drink = "Лимонад 🥤"
        price = LEMONADE_PRICE
    case _:
        drink = None
        price = 0

match drink:
    case None:
        print("⚠️ Ошибка: такого напитка нет в меню.")
    case _:
        quantity_text = input("Введите количество порций: ")

        match quantity_text:
            case "1":
                quantity = 1
            case "2":
                quantity = 2
            case "3":
                quantity = 3
            case "4":
                quantity = 4
            case "5":
                quantity = 5
            case "6":
                quantity = 6
            case "7":
                quantity = 7
            case "8":
                quantity = 8
            case "9":
                quantity = 9
            case "10":
                quantity = 10
            case _:
                quantity = 0

        match quantity:
            case 0:
                print("⚠️ Ошибка: введите число порций от 1 до 10.")
            case _:
                discount_code = input(
                    "Введите код скидки: "
                )

                match discount_code:
                    case "":
                        discount = 0
                        discount_text = "Нет"
                    case "SALE10" | "sale10":
                        discount = 10
                        discount_text = "10%"
                    case "SALE20" | "sale20":
                        discount = 20
                        discount_text = "20%"
                    case _:
                        discount = 0
                        discount_text = "Нет (код не распознан)"

                total = price * quantity
                discount_amount = total * discount / 100
                final_total = total - discount_amount

                match quantity:
                    case 1:
                        portion_word = "порция"
                    case 2 | 3 | 4:
                        portion_word = "порции"
                    case _:
                        portion_word = "порций"

                print("\n" + "=" * 45)
                print("             🧾 ВАШ ЧЕК")
                print("=" * 45)
                print(f"Напиток:             {drink}")
                print(f"Цена за порцию:      {price} руб.")
                print(f"Количество:          {quantity} {portion_word}")
                print(f"Сумма:               {total:.2f} руб.")
                print(f"Скидка:              {discount_text}")
                print(f"Размер скидки:       {discount_amount:.2f} руб.")
                print("-" * 45)
                print(f"К ОПЛАТЕ:            {final_total:.2f} руб.")
                print("=" * 45)
                print("       Спасибо за покупку! 😊")