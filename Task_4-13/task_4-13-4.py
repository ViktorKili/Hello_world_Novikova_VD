N = int(input("Введите N: "))
if N < 1:
    print("нет суммы")
else:
    max = 0
    i = 1
    while i <= N:
        max = max + i
        i = i + 1
    print(max)