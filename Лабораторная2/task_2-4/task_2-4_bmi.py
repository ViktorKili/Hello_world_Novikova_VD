weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)
print("\n---Отчет о состоянии здоровья")
print(f"Рост\t\t{height}м")
print(f"Вес\t\t{weight}kg")
print(f"Индекс массы тела: {bmi:.2f}")