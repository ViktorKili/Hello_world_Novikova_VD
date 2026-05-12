N = int(input("Введите N: "))
if N <= 0:
    print("N должно быть >= 0")
else:
    sum = 0
    i = 1
    while i <= N:
        sum = sum + i ** 2
        i = i + 1
    print(sum)