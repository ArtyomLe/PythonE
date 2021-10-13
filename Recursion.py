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
# NOD => НАИБОЛЬШИЙ ОБЩИЙ ДЕЛИТЕЛЬ
def nod(a, b):
    while(a != 0 and b != 0):
        if(a > b):
            a %= b
        else:
            b %= a
    return a + b

print(nod(7, 13))                  # Вызываем функию НОД и печатаем её результат
