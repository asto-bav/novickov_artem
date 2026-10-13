# Константы для нормальных показателей
TEMP_MIN = 36
TEMP_MAX = 37
PRESSURE_MIN = 110
PRESSURE_MAX = 130
PULSE_MIN = 60
PULSE_MAX = 100


try:
    temperature = float(input("Введите температуру (°C): "))
    pressure = int(input("Введите верхнее давление: "))
    pulse = int(input("Введите пульс (уд/мин): "))

    if not (-50 <= temperature <= 60 and
            0 < pressure < 300 and 0 < pulse < 300):
        print("Ошибка ввода: некорректные показатели.")

    elif (temperature < 35 or temperature > 38 or
          pressure < 105 or pressure > 140 or
          pulse < 55 or pulse > 110):
        print("Требуется врач.")

    elif (TEMP_MIN <= temperature <= TEMP_MAX and
          PRESSURE_MIN <= pressure <= PRESSURE_MAX and
          PULSE_MIN <= pulse <= PULSE_MAX):
        print("Нормальное состояние.")

    else:
        print("Легкое недомогание.")

except ValueError:
    print("Ошибка ввода: введите числовые значения.")