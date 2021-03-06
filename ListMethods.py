# Добавить в конец (append)
a = [12, 32]
a.append(4)
print(a)
# Вывод [12, 32, 4]

# ============================

# Вставка до (insert)
a = [32, 43, 56, 432]
a.insert(2, 23) # первая цифра указывает на индекс числа в списке перед которым вставим вторую цифру
print(a)
# Вывод [32, 43, 23, 56, 432]

# ============================

# Сортировка значений (sort)
a = [1, 5, 3, 2, 4]
a.sort() # reverse=True (Получаем сортировку в порядке убывания) но есть и отдельный метод (reverse)
print(a)
# Вывод [1, 2, 3, 4, 5]

# ============================

# Удалить все элементы (clear)
a = [1, 2, 3, 4, 5]
print(a)
a.clear() # Удаляет все элементы но при этом сохраняет список(пустым)
print(a)
# Вывод [1, 2, 3, 4, 5]
#       []

# ============================

# Удалить элемент (pop)
a = [5, 4, 3, 2, 1]
a.pop(2) # Индекс удаляемого элемента
print(a)
# Вывод [5, 4, 2, 1]

# ============================

# Удалить по значению (remove)
a = [5, 4, 3, 2, 1]
if (4 in a): # Есть ли в списке a цифра 4 то: (Проверять желательно, но не обязательно)
    a.remove(4)
print(a)
# Вывод [5, 3, 2, 1]

# ============================

# Копия списка (copy)
a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)
# Вывод [1, 2, 3, 4, 5]

# =============================

# Подсчёт кол-ва (count)
a = [1, 2, 2, 2, 1]
b = a.count(1) # Сколько раз в списке встречается элемент со значением 1
print(b)
# Вывод 2

# =============================

# Расширить список (extend)
a = [0, 1, 2]
s = "AbC"
a.extend(s)
print(a)
# Вывод [0, 1, 2, 'A', 'b', 'C']

# =============================

# Получить индекс (index)
a = [5, 3, 3, 3, 4]
b = a.index(3)  # Возвращает первый встречный номер найденного элемента
print(b)
# Вывод 1
# Или
a = [5, 3, 3, 3, 4]
try:
    b = a.index(7)
    print(b)
except:
    print("Элемент не найден!")
# Вывод Элемент не найден!

# ================================

# Перевернуть список (reverse)
a = [5, 4, 3, 2, 1]
a.reverse()
print(a)
# Вывод [1, 2, 3, 4, 5]

# ================================

# Генераторы

a = []
for i in range(8):
    a.append(i)
print(a) # Получаем [0, 1, 2, 3, 4, 5, 6, 7]

# Существует так же сокращение
a = [i for i in range(8)]
print(a) # Так же получаем [0, 1, 2, 3, 4, 5, 6, 7]

# Заполняем нулями
a = [0 for i in range(8)]
print(a) # Получаем [0, 0, 0, 0, 0, 0, 0, 0]

# Если вместо 0 в прошлом примере подставить счётчик, то можно создать двумерный список
# Создадим к примеру список 3x3 заполненый нулями
a = [[0 for i in range(3)] for i in range(3)]
print(a)
# Получаем [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a = [[j for i in range(3)] for j in range(3)]
print(a)
# Получаем [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

# список = [ЭЛЕМЕНТ for i in range(КОЛИЧЕСТВО)]
# Элемент может быть динамичным

# Формируем таблицу умножения
#         кол-во столбцов                 кол-во строк (j увелич. на 1 каждые 9 итераций i)
a = [[(i * j) for i in range(1, 10)] for j in range(1, 10)]
print(a)
# [[1, 2, 3, 4, 5, 6, 7, 8, 9],             # (i*j) 1x1, 2x1, 3x1...9x1
#  [2, 4, 6, 8, 10, 12, 14, 16, 18],        # (i*j) 1x2, 2x2, 3x2...9x2
#  [3, 6, 9, 12, 15, 18, 21, 24, 27],       # (i*j) 1x3, 2x3, 3x3...9x3
#  [4, 8, 12, 16, 20, 24, 28, 32, 36],
#  [5, 10, 15, 20, 25, 30, 35, 40, 45],
#  [6, 12, 18, 24, 30, 36, 42, 48, 54],
#  [7, 14, 21, 28, 35, 42, 49, 56, 63],
#  [8, 16, 24, 32, 40, 48, 56, 64, 72],
#  [9, 18, 27, 36, 45, 54, 63, 72, 81]]

# Чтобы не присутствовал ноль - range(1, 10)

#           *   *   *   *   *

# Некоторые дополнительные примеры
#      кол-во столбцов          кол-во строк
a = [[(j*i) for i in range(5)] for j in range(1, 4)] # Здесь 3 строки
print(a)
# Вывод [[0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]

a = [[(j*i) for i in range(1, 5)] for j in range(4)] # Здесь строк уже 4
print(a)
# Вывод [[0, 0, 0, 0], [1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]