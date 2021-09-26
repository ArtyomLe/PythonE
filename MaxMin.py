import random
line = 5
colm = 9
a = []
for i in range(line):
    a.append([])
    for n in range(colm):
        a[i].append(random.randint(10, 99))

