print("=" * 45)
print("          📦 ОТСЛЕЖИВАНИЕ ЗАКАЗА")
print("=" * 45)

status = input("Введите статус заказа (pending, processing, shipped, delivered, cancelled): ")

match status:
    case "pending":
        name = "В ожидании"
        description = "Заказ принят и ожидает обработки."
        emoji = "⏳"
        waiting_time = 30
    case "processing":
        name = "В обработке"
        description = "Заказ собирается и подготавливается."
        emoji = "⚙️"
        waiting_time = 120
    case "shipped":
        name = "Отправлен"
        description = "Заказ передан службе доставки."
        emoji = "🚚"
        waiting_time = 600
    case "delivered":
        name = "Доставлен"
        description = "Заказ успешно доставлен получателю."
        emoji = "✅"
        waiting_time = 0
    case "cancelled":
        name = "Отменён"
        description = "Заказ отменён."
        emoji = "❌"
        waiting_time = 0
    case _:
        name = None
        description = "Указан неизвестный статус."
        emoji = "⚠️"
        waiting_time = 0

print("\n" + "=" * 45)
print("          ИНФОРМАЦИЯ О ЗАКАЗЕ")
print("=" * 45)

match name:
    case None:
        print(f"{emoji} Ошибка: {description}")
        print("Проверьте правильность введённого статуса.")
    case _:
        print(f"Статус: {name} {emoji}")
        print(f"Описание: {description}")

        match waiting_time:
            case 0:
                print("Время ожидания: отсутствует")
            case _:
                print(f"Примерное время ожидания: {waiting_time} мин.")
print("Рекомендация: Следите за уведомлениями о доставке")
print("=" * 45)