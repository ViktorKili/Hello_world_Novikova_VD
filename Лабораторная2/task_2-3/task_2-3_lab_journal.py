# Электронный лабораторный журнал
fio = input ("Напишите ФИО исследователя: ")
date = input ("Напишите дату исследования: ")
experement = input ("Введите название эксперимента: ")
result = input ("Вывод: ")
                

print("Запись данных в журнал")
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"|{'Электронный лабораторный журнал':<50}|\n")

    file.write("+" + "-" * 50 + "+\n")
    file.write(f"|{'ФИО исследователя: '+ fio:<50}|\n")
    file.write(f"|{'Дата исследования: '+ date:<50}|\n")
    file.write(f"|{'Название эксперемента: '+ experement:<50}|\n")

    file.write("+" + "-" * 50 + "+\n")
    file.write(f"|{'Вывод: '+ result:<50}|\n")

    print("Данные успешно сохранены в файл journal.txt")
