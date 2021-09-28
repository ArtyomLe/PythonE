# Первый способ(for)
list2D = [[10, 15, 25, 20, 30], [52, 11, 17, 63, 25], [14, 28, 10, 10, 17]]

p1 = -1
p2 = 0

for i in range(3):
    for j in range(5):
        if(list2D[i][j] % 17 == 0):
            if (p1 == -1):
                p1 = i
                p2 = j
if (p1 != -1):
    print(f"Индексы первого кратного 17 элемента [{p1}][{p2}]")
else:
    print("Кратных 17 нет.")

# Второй способ(while)

list2D = [[10, 15, 25, 20, 30], [52, 11, 17, 63, 25], [14, 28, 10, 10, 17]]
find = False
x = 0

while(x < len(list2D) and not find):
    y = 0
    while (y < len(list2D[x]) and not find):
        if (list2D[x][y] % 17 == 0):
            find = True
        y += 1
    x += 1

x -= 1
y -= 1

if (find):
    print(f"Индексы первого кратного 17 элемента [{x}][{y}]")
else:
    print("Кратных 17 нет.")
