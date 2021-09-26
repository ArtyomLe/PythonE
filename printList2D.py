import random
def printList2D(lst):
    for i in range(len(lst)):
        for m in range(len(lst[i])):
            print(f"{lst[i][m]} ",end="")
        print()

line = 5
colm = 9

a=[]

for i in range(line):
    a.append([])
    for k in range(colm):
        a[i].append(random.randint(10, 99))

printList2D(a)