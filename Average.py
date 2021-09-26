import  random

n = 70
m = 12

a = []

average = 0
count = 0

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(20000, 150000))
        average += a[i][j]                # Здесь получаем общую сумму

average /= n*m                            # Здесь получаем среднюю сумму(Общую сумму делим на кол-во ячеек в списке)

for i in range(n):                        # Считаем, перебирая с помощью цикла в цикле значения каждого элемента списка
    for k in range(m):
        if(a[i][k] > average):            # Ежели выше среднего, то заносим в переменную count
            count += 1

print("Средняя зарплата: ", int(average)) # int На случай если число получится дробным (или // в строке средней суммы)
print(f"Кол-во зарплат выше средней: {count}")