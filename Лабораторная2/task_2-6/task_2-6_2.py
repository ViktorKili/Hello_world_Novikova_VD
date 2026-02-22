temp = float(input("Какая температура листа сейчас? "))

if temp < 5:
    print("Слишком холодно, фотосинтез почти не идет.")
elif 5 <= temp <= 25:
    print("Оптимально для растений с С3-метабализмом")
elif 25 < temp <= 35:
    print("Хорошо для растений с С4-метаболизмом")
else:
    print("Holy-Moly! Cool down, bro!")
