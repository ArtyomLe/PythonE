# По разному зашифровываем одно и тоже число

def getData(a):
    d = 0
    length = len(a)
    for i in range(length):
        d += a[i] * 10 ** i
    return d

def printData(a):
    for i in range(len(a) - 1, -1, -1):
        print(f" {a[i]}", end="")
    print()

print("Обычное число")
a = [4, 6, 9, 8, 5, 5]
printData(a)
print(getData(a))

print("\nЗашифрованное число")
a = [54, 21, 67, 12, 54]     # 54 + 210 + 6700 + 12000 + 540000
printData(a)
print(getData(a))

