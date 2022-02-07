# File name func_param.py

def printMax(a, b):       # Здесь a&b это параметры
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

printMax(3, 4)  # Прямая передача значений

x = 7
y = 5

printMax(x, y)  # Передачаа переменных в качестве аргументов
