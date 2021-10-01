def isDigit(s):
    res = True
    startCode = ord("0") # 48 юникод
    stopCode = ord("9")  # 57 юникод
    p = 0
    while(p < len(s) and res):
        if (ord(s[p]) < startCode or ord(s[p]) > stopCode):
            res = False
        p += 1
    return res

stroka = "123123"
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")

stroka = "1000.23" # Обратите внимание что помимо цифр в строке есть точка
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")

stroka = "Я строка" # Обратите внимание что помимо цифр в строке есть пробел
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")

print("\n")
# =================================================================================

codeList = []
for i in "WASDE01234":
    codeList.append(ord(i))
# print(codeList) # => [87, 65, 83, 68, 69, 48, 49, 50, 51, 52]

command = input("Введите комманды Копатыча: ")
cleanCommand = ""

for i in command: # Проверяем счётчиком цикла каждый символ в строке команд последовательно
    if(ord(i) in codeList): # принцип ("А" in "ALPHABET") => True
        cleanCommand += i
print(f"Очищенная строка для Копатыча: {cleanCommand}")


print("\n")
# =====================================================================
"""
# Сумма чисел значения
summa = 0
num = 10000

for i in range(1, num +1):
    summa += i
print(summa)

print("\n")
# =======================
n = 10000
sum=n*(n+1)//2
print(sum)

print("\n")
# =======================
a = ""
while(not a.isdigit()):
    a = input("Введите целое число: ")
a = int(a)
print(a)

print("\n")

# ========================
def isDigit(s):
    res = True
    startCode = ord("0") # 48
    stopCode = ord("9")  # 57
    p = 0
    while(p < len(s) and res):
        if (ord(s[p]) < startCode or ord(s[p]) > stopCode):
            res = False
        p += 1
    return res


# chr(число в символ юникода) в скобках пишем без ковычек
# ord("антипод chr") в скобках пишем с ковычками потому что это символ таблицы а не число

start = ord("0")  # 0 это будет символ юникода 48
for i in range(10):
    print(f"{chr(start + i)} = {start + i}")

# print(start) выведет 48
# print(chr(48)) выведет 0
# ============================
"""