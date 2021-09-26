import random
line = 5
colm = 9
a = []
for i in range(line):
    a.append([])
    for n in range(colm):
        a[i].append(random.randint(10, 99))

max_value = a[0][0]
min_value = a[0][0]

for i in range(line):
    for j in range(colm):
        if(a[i][j] > max_value):
            max_value = a[i][j]
        if(a[i][j] < min_value):
            min_value = a[i][j]
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")