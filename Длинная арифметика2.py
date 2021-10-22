# Перевод в различные системы счисления
def getData(a, osnovsnie):
    d = 0
    length = len(a)
    for i in range(length):
        d += a[i] * osnovsnie ** i # ФОРМУЛА:   < Цифра числа * Основание^ Позиция цифры >
    return d

# def printData(a):
#     for i in range(len(a) - 1, -1, -1):
#         print(f" {a[i]}", end="")
#     print()

# a = [3, 2, 1]
a = [0, 0, 0, 0, 1]
print(getData(a, 16))

# ===========================================================================================

d = 10
raz = 1077
for i in range(raz):
    d /= 2
    print(f"После деления: {d}")

for i in range(raz):
    d *= 2
    print(f"После умножения: {d}")