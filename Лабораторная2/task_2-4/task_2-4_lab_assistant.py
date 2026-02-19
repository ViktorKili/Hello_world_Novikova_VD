volume = float(input("Введите нужный объем раствора: "))
salt = volume*0.009
rounded = round(salt,2)
water = volume
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-------------------")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли: {rounded} г\n")
    file.write(f"Объем воды: {water} ил\n")

print(f"\nРецепт успешно сохранен в файл recipe.txt")
print(f"Для приготовления {volume} мл 0.9% физиологического раствора потребуется: ")
print(f" - Соль: {rounded} г")
print(f" - Вода: {water} мл")