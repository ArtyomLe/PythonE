#!/usr/bin/python
# File name func_doc.py

def printMax(x, y):
    '''Выводит максимальное из двух чисел.

     Оба значения должны быть целыми числами.'''
    
    x = int(x) # Конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__) # аналогично help(printMax)


