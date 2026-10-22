print("=" * 40)
print("      ⭐ РЕЙТИНГ ПРОДУКТА ⭐")
print("=" * 40)

rating = input("Введите рейтинг продукта (1–10): ")

match rating:
    case "9" | "10":
        description = "Отличный"
        emoji = "🌟"
        recommendation = "Рекомендую!"
    case "7" | "8":
        description = "Хороший"
        emoji = "😊"
        recommendation = "Рекомендую!"
    case "4" | "5" | "6":
        description = "Средний"
        emoji = "😐"
        recommendation = "Можно попробовать."
    case "1" | "2" | "3":
        description = "Плохой"
        emoji = "😞"
        recommendation = "Не рекомендую."
    case _:
        description = None
        emoji = "⚠️"
        recommendation = "Введите число от 1 до 10."

print("\n" + "=" * 40)

match description:
    case None:
        print(f"{emoji} Ошибка: {recommendation}")
    case _:
        print(f"Рейтинг: {rating}/10")
        print(f"Оценка: {description} {emoji}")
        print(f"Рекомендация: {recommendation}")

print("=" * 40)