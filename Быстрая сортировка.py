
def qsort(a):
    if (len(a) == 2):
        if (a[0] > a[1]):
            a[0], a[1] = a[1], a[0]
        return a

    elif (len(a) > 2):
        average = sum(a) // len(a)  # Считаем среднее

        sp1 = []                        # Элементы меньше среднего
        sp2 = []                        # Элементы равные среднему
        sp3 = []                        # Элементы больше среднего

        for i in a:
            if (i < average):
                sp1.append(i)
            elif (i > average):
                sp3.append(i)
            else:
                sp2.append(i)

        return qsort(sp1) + sp2 + qsort(sp3)

    else:
        return a

a = [5, 8, 1, 5, 3, 5, 2, 0, 5, 2]
print(a)
a = qsort(a)
print(a)

"""
1) Находим среднее арифметическое.

2) Если список длинной меньше двух элементов, то возвращаем его с помощью return.

3) Если список содержит два элемента,то сортирруем его в порядке возврастания(или убывания в зависимости от потребности)

4) Если список длиной больше двух элементов, то разбиваем его. Распределим элементы так, чтобы в одном списке оказались
    меньшие среднему арифметическому значения, во втором - равные, в третьем - превышающие среднее арифметическое.

5) В return отправляем полученые списки в текущую функцию, заставляя выполнить алгоритм с пункта №1 для каждого списка,
   кроме списка равных среднему арифметическому элементов.

"""

# Для экономии ресурсов процессора, можно не высчитывать каждый раз среднее арифметическое

def qsort(a):
    if (len(a) == 2):
        if (a[0] > a[1]):
            a[0], a[1] = a[1], a[0]
        return a
    elif (len(a) > 2):
        average = a[len(a) // 2] # просто берём элемент по центру списка
        print(average)

        sp1 = []                 # Элементы меньше среднего
        sp2 = []                 # Элементы равные среднему
        sp3 = []                 # Элементы больше среднего

        for i in a:
            if (i < average):
                sp1.append(i)
            elif (i > average):
                sp3.append(i)
            else:
                sp2.append(i)
        return qsort(sp1) + sp2 + qsort(sp3)
    return a

a = [5, 8, 1, 5, 3, 5, 2, 0, 5, 2]
print(a)
a = qsort(a)
print(a)

"""
def sp(spisok):
    spisok[0] = "Хех!"

a = [1, 2, 3]
print(a)
# sp(a)
a[0] = "Хэх!"
print(a)
"""
print("\n")


def qsort(a, startElement, endElement):
    # Если левая граница больше правой, то прерываем метод с помощью return
    if (startElement >= endElement):
        return

    # Вычисляем average
    # 1. С помощью среднего арифметического списка a
    average = sum(a[startElement:endElement]) // (endElement - startElement)
    # 2. С помощью центрального элемента списка a
    # average = a[startElement + (endElement - startElement) // 2]

    first = startElement
    last = endElement

    while (first <= last):
        # Находим индекс левого элемента, который больше или равен опорному числу
        while (a[first] < average):
            first += 1
        # Находим индекс правого элемента, который меньше или равен опорному числу
        while (a[last] > average):
            last -= 1

        if (first <= last):
            a[first], a[last] = a[last], a[first]
            first += 1
            last -= 1

    qsort(a, startElement, last) # Левая часть списка
    qsort(a, first, endElement)  # Правая часть списка

a = [5, 8, 1, 5, 3, 5, 2, 0, 2, 5, 2]
print(a)
qsort(a, 0, len(a) - 1) # 0 == startElement(индекс левой границы списка) | len(a)-1 == endElement(индекс правой границы)
print(a)

