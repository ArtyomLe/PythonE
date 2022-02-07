#!/usr/bin/python
# File name func_return.py

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'מספרים שווים'
    else:
        return y

print(maximum(4, 2))
