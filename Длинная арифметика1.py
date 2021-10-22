
def getData(a):
    d = 0
    length = len(a)

    for i in range(length):
        d += a[i] * 10 ** i
    return d

a = [54, 21, 67, 12, 54]
print(getData(a))
a = [4, 6, 9, 8, 5, 5]
print(getData(a))