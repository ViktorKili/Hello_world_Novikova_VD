# Запрос данных
fio = input("Имя оператора: ")
current_number = input("Текущее значение датчика давления (Па): ")

# Запись данных в файл
with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Введите имя оператора: {fio}\n")
    file.write(f"Введите текущее значение давления (Па): {current_number}")

print("Данные успешно сохранены в sensor_log.txt")