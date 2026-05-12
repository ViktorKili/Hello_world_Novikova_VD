N = int(input("Введите N: "))
if N < 0:
    print("N должно быть > 0")
else:
    sum = 1
    i = 1
    while i <= N:
        sum = sum * i
        i = i + 1
    print(sum)