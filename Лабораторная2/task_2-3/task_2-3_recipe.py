# Запрос данных

name = input("Название питательной среды: ")
concentration = input("Концентрация агар-агара (%): ")
temperature = input("Температура стерилизации: ")

# Запись данных в файл
with open("recipe.txt", "w", encoding="utf-8") as card: 
    card.write(f"{name}\n") 
    card.write("Параметры:\n")
    card.write(f"Концентрация агара: {concentration}%\n")
    card.write(f"Температура стерилизации: {temperature}\n")

print("Файл 'recipe.txt' успешни сформирован!")