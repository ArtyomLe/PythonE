from tkinter import *

def goDecode():
    if (rBtn.get() == 0 or rBtn.get() == 1):
        goCode()
    else:
        tOutput.delete(1.0, END)
        tIn = tInput.get(1.0, END)
        tIn = tIn[0:len(tIn) - 1]
        tOut = ""
        if (rBtn.get() == 2):
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - 1)
        elif (rBtn.get() == 3):
            p = 0
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - p)
                p = (p+1) % 33
        tOutput.insert(1.0, tOut)


def goCode():
    tOutput.delete(1.0, END)
    tIn = tInput.get(1.0, END)
    tIn = tIn[0:len(tIn) - 1]                   # Убираем перенос строки
    tOut = ""
    if (rBtn.get() == 0):
        for i in range(len(tIn) - 1, -1, -1):
            tOut += tIn[i]                      # Инверсия
    elif (rBtn.get() ==  1):
        for i in range(len(tIn) - 1, 2):
            tOut += tIn[i + 1] + tIn[i]         # Замена с соседней
    elif (rBtn.get() == 2):
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + 1)        # Увеличение кода символа на 1
    elif (rBtn.get() == 3):
        p = 0
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + p)        # Смещение по коду циклически до 33
            p = (p + 1) % 33
    tOutput.insert(1.0, tOut)

def clearText():

def resToDef():

def pasteFromClipboard():

def copyToClipboard():

def setMenuPos():

# ----------------------------------------------------------------------------------------------------------------------
# Инициализация окна
root = Tk()
root.resizable(False, False)
root.title("Шифровщик")

# Настройка геометрии окна
WIDTH = 800
HEIGHT = 320
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
# ----------------------------------------------------------------------------------------------------------------------
# Текстовые метки
textInput = Label(text="Введите исходный текст:")
textInput.place(x=2, y=1)
textOutput = Label(text="Результат:")
textOutput.place(x=2, y=157)

# Текстовые поля
tInput = Text(width=70, height=8, wrap=WORD)              # Размеры окна ввода
tInput.place(x=5, y=20)                                   # Начало координат окна ввода
tInput.insert(1.0, """Экземпляры Checkbutton также могут быть визуально оформлены в группу,
но каждый флажок независим от остальных. Каждый может быть в состоянии "установлен" или "снят",
независимо от состояния других флажков. Другими словами в группе Checkbutton можно сделать
множественный выбор, в группе Radiobutton - нет.""")
scrollInput = Scrollbar(command=tInput.yview, width=20)   # Переменная полосы прокрутки ввода
scrollInput.place(x=570, y=20, height=132)                # Позиция на экране полосы прокрутки ввода
tInput["yscrollcommand"] = scrollInput.set
# = = = = = = = = = = = = = = = = = = = = =
tOutput = Text(width=70, height=8, wrap=WORD)             # Размеры окна вывода
tOutput.place(x=5, y=180)                                 # Начало координат окна вывода

scrollOutput = Scrollbar(command=tOutput.yview, width=20) # Переменная полосы прокрутки вывода
scrollOutput.place(x=570, y=180, height=132)              # Позиция на экране полосы прокрутки вывода
tOutput["yscrollcommand"] = scrollOutput.set

# Меню на правую кнопку
menuInput = Menu(tearoff=False)                                                # Задаём переменную на меню правой кнопки
menuInput.add_command(label="Копировать результат", command=copyToClipboard)      # Что выводит в меню на первой строчке
menuInput.add_command(label="Вставить в исходный текст", command=pasteFromClipboard) # и какие функции при этом вызываем
menuInput.add_command(label="Результат -> Исходный", command=resToDef)               # всего 4 опции и у каждой функция
menuInput.add_command(label="Очистить текст", command=clearText)
tInput.bind("<Button-3>", setMenuPos)

# Две правые кнопки шифрования\дешифрования вверху на чекбоксами
btnCode = Button(text="Шифровать", width=25, command=goCode)       # Переменная для кнопки шифрования справа вверху
btnCode.place(x=600, y=20)                                         # позиция в окне

btnDecode = Button(text="Дешифровать", width=25, command=goDecode) # Переменная для кнопки дешифрования справа вверху
btnDecode.place(x=600, y=50)                                       # позиция в окне

# Радиокнопки(checkbox)
textAlgo = Label(text="Алгоритм:")
textAlgo.place(x=600, y=100)
rBtn = IntVar()
rBtn.set(0)

algo01 = Radiobutton(text="Инвертировать", variable=rBtn, value=0)      # Задаём переменные со значениями (0 -> 3)
algo02 = Radiobutton(text="Замена с соседней", variable=rBtn, value=1)
algo03 = Radiobutton(text="+1", variable=rBtn, value=2)
algo04 = Radiobutton(text="+позиция (до 33)", variable=rBtn, value=3)

algo01.place(x=600, y=120)                                              # Расположение радиокнопок в окне (1 -> 4)
algo02.place(x=600, y=140)
algo03.place(x=600, y=160)
algo04.place(x=600, y=180)
# ----------------------------------------------------------------------------------------------------------------------
# mainloop
root.mainloop()

