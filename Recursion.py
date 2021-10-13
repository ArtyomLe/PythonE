'''
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
'''
# NOD => НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ(Функция)
def nod(a, b):
    while(a != 0 and b != 0): # 75   and   30 | 15   and   30 | 15   and   0  |               |
        if(a > b):            #               |               |               |               |
            a %= b            # a = 75%30(15) |               |               |               |
        else:                 #               |               |               |               |
            b %= a            #               | b = 30%15(0)  |               |               |
    return a + b              #               |               |return 15+0(15)|               |

print(nod(75, 30))                  # Вызываем функию НОД и печатаем её результат


# NOD => НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ(Рекурсия)
def nod(a, b):
    if(a == 0 or b == 0):
        return a + b
    if (a > b):
        return nod(a % b, b)
    else:
        return nod(a, b % a)

print(nod(75, 30))
