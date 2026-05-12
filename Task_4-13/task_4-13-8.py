N = int(input("Введите N: "))
if N <= 0:
    print("N должно быть > 0")
else:
    sum = 0
    i = 1
    while i <= N:
        x = float(input("Введите число: "))
        if x > 0:
            sum = sum + 1
        i = i + 1
    print(sum)