"""
def req(n):    # 5 => n | print 5 | 5 > 0 | 5 - 1 = 4 | print 4 ...
    print(n)
    if(n > 0):
        req(n - 1)
req(5)

print("\n")

def req(n):
    print(n)
    if(n < 4):
        req(n + 1)
    print(n)
req(0)

print("\n")

def req(n):
    print(n)
    if(n < 4):
        req(n + 1)
    print(n)
req(0)


# NOD => НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ(Функция)
def nod(a, b):
    while(a != 0 and b != 0): # 75   and   30 | 15   and   30 |  15   and   0   |               |
        if(a > b):            #               |               |                 |               |
            a %= b            # a = 75%30(15) |               |                 |               |
        else:                 #               |               |                 |               |
            b %= a            #               | b = 30%15(0)  |                 |               |
    return a + b              #               |               | return 15+0(15) |               |

print(nod(75, 30))                  # Вызываем функию НОД и печатаем её результат


# NOD => НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ(Рекурсия)
def nod(a, b):
    if(a == 0 or b == 0):     #      75    and    30      |      15    and    30      |     15    and    0      |
        return a + b          #                           |                           |   return 15 + 0 (15)    |
    if (a > b):               #                           |                           |                         |
        return nod(a % b, b)  # return nod(75%30(15), 30) |                           |                         |
    else:                     #                           |                           |                         |
        return nod(a, b % a)  #                           | return nod(15, 30%15(0) ) |                         |

# return nod  =>   Вернёт значения в начало функции def nod(a, b) т.е это цикл который выполняется внутри самой функции
# return      =>              Вернёт значения за пределы функции туда откуда она была изначально вызвана
print(nod(75, 30))                  # Вызываем функию НОД и печатаем её результат


# Ещё примеры рекурсии(Вычисление суммы чисел)

def sumDigit(n):
    if (n > 0):       # В случае верности данного условия мы должны вернуть сумму текущей цифры и результата следующей рекурсии
        return n % 10 + sumDigit(n // 10) # 354%10=4 + sumDigit(354//10)=35   ==>> def sumDigit(35)
                                          # 35%10= 5 + sumDigit(35//10)= 3    ==>> def sumDigit(3)
                                          # 3%10 = 3 + sumDigit(3//10) = 0    ==>> def sumDigit(0) False
                                          # Условие if (n > 0) больше не верно, рекурсия захлопывается 4 + 5 + 3 + 0
#  Результат: 12                return 4 + 5 (8)
#                                   return 5 + 3 (3)
#                                       return 3 + 0 (return)
    else:
        return 0


print(sumDigit(354))

# Через while(Вычисление суммы чисел)

def sumDigit(n):
    summa = 0
    while (n > 0):
        summa += n % 10
        n //= 10
    return summa

print(sumDigit(354))
"""
# Рекурсия вывод отдельных чисел =>    COPY          =>       COPY         =>          COPY        =>          COPY
def sumDigit(n):            # sumDigit(354):         | sumDigit(35):         | sumDigit(3):         | sumDigit(0):   |
    if (n > 0):             #   if (354 > 0):        |   if (35 > 0):        |    if (3 > 0):       |   if (0 > 0):  |
        sumDigit(n // 10)   #       sumDigit(354//10)|      sumDigit(35//10) |      sumDigit(3//10) |      false     |
        print(n % 10)       #     print(n%10) = 4   <=   print(n%10) = 5   <=   print(n%10) = 3  <= Возвращение рекурсии

sumDigit(354)

