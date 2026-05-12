N = int(input("Введите N: "))
if N <= 0:
    print("N должно быть > 0")
else:
    sum = 0
    i = 1
    while i <= N:
        x = float(input("Введите число: "))
        sum = sum + x
        i = i + 1
    avg = sum / N
    print(avg)