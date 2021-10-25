
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
print("\n")

# ++++++++++++++++++++++++++++++

def f(w):
    s = 0
    for i in range(len(w)):     # len(w) = 4     =>  ((1, 4) - (5, 1))
        s += w[i]               # s = 0+1(1) => s = 1+4(5) => s = 5 -5(0) => 0 -1(-1)  *** f(h)=5   -   f(p)=-6 ***
#        print(w[i])
    return s
h = [1, 4]
p = [5, 1]
print(f(h) - f(p))
