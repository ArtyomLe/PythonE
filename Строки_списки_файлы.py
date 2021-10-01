
#                  Полный код функции возвращающей двумерный список из содержимого файла

def getFileString(filename):
    ret = []                                      # Создаём список, который вернём
    try:                                          # Потенциально небезопасная ситуация(используем try)
        f = open(filename, "r", encoding="utf-8") # Получаем "паспорт" файла в переменную f дескриптор
        for line in f.readlines():                # Обрабатываем каждую строку информации из файла
            line = line.replace("\n", ""))        # Убираем вертикальный пробел "/n" заменяя его ""
            line = line.split("#")                # Разбиваем строку по знаку # и заносим в одномерный список
            ret.append(line)                      # Создаём двумерный очищенный список
        f.close()                                 # Закрываем паспорт дескриптор
    except:
        print("Ошибка открытия файла! Проверьте правильность имени и пути.")
    return ret


#                                            Пояснения ниже
"""
def getFileString(filename):
    ret = []                                      # Создаём список, который вернём
    try:                                          # Потенциально небезопасная ситуация(используем try)
        f = open(filename, "r", encoding="utf-8") # Получаем "паспорт" файла в переменную f дескриптор
        for line in f.readlines():                # Обрабатываем каждую строку информации из файла
            line = line.replace("\n", ""))        # Убираем вертикальный пробел "/n" заменяя его ""
            line = line.split("#")                # Разбиваем строку по знаку # и заносим в одномерный список 
            ret.append(line)                      # Создаём двумерный очищенный список
        f.close()                                 # Закрываем паспорт дескриптор
    except:
        print("Ошибка открытия файла! Проверьте правильность имени и пути.")
    return ret                                    # Возвращаем сформированный список

#                            *       *       *       *       *       *       *
# "управляющий" "переменная/счётчик линий"   "дескриптор f.readlines и метод чтения из файла списка строк"
#       for           line                              in  f.readlines():               Это переборная конструкция


# Почему line.replace("\n", "") а не просто line. Для избегания вертикальных пробелов при составлении строк списка
# Георгиев Г.#3#3#2#3#4#3#2
#  отменяем пробел( "\n" )
# Ефремов Е.#4#3#н#н#н#3#4#4#4
# =================================================================================================================
#                       Разбить строку по знаку(символу) # и поместить результат в список
#                                   "1#2#3" => ["1", "2", "3"]
#           Метод =>    строка.split(символ[, maxsplit=число])

a = "Привет#.# #мир#!"
a = a.split("#") # без maxsplit
print(a) # ['Привет', '.', ' ', 'мир', '!']
# =========================================
a = "Привет#.# #мир#!"
a = a.split("#", maxsplit=3)
print(a) # ['Привет', '.', ' ', 'мир#!']
"""