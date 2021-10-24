
def f(p):
    if(p <= 0):
        return 0
    return f(p - 2) + p
print(f(5))

# ++++++++++++++++++++++++++++

b = []

b.append([56, 20, 20, 81])
b.append([30, 31, 84, 12])
b.append([91, 31, 35, 85])
b.append([17, 87, 92, 42])
b.append([64, 70, 75, 90])

s = 0
for i in range(5):
    for j in range(4):
        if (b[i][j] % 5 != 0):
            s += 1
print(s)