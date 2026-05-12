N = int(input("Введите N: "))
if N <= 0:
    print("N должна быть > 0")
else:
    sum = 0
    i = 1
    while i <= N:
        x = int(input("Введите число: "))
        if i % 2 != 0: 
            sum = sum + x
        i = i + 2
    print(sum)