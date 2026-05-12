N = int(input("Введите N: "))
if N <= 0:
    print("N должно быть больше 0")
else:
    max_val = float(input("Введите число 1: "))
    i = 1
    while i < N:
        x = float(input(f"Введите число {i + 1}: "))
        if x > max_val:
            max_val = x
        i = i + 1
    print(f"Максимум: {max_val}")