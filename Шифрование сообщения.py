import random
toCode = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
sIn = input("Введите строку для шифрования: ").upper()
sOut = ""

for i in range(len(sIn)):
    count = random.randint(0, 10)
    for j in range(count):
        sOut += toCode[random.randint(0, len(toCode) - 1)]
    if (random.randint(0, 1) == 1):
        sOut += "А"
    else:
        sOut += "Б"
    sOut += sIn[i]
print(f"Зашифрованная строка: {sOut}")