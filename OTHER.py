
def f(p):
    if(p <= 0):
        return 0
    return f(p - 2) + p
print(f(5))
