A = float(input("Введите X: "))
B = float(input("Введите Y: "))
C = float(input("Введите Z: "))
D = float(input("Введите T: "))
min_val = A
if B < min_val:
    min_val = B
if C < min_val:
    min_val = C
if D < min_val:
    min_val = D

print(min_val)