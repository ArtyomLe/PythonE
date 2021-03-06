from tkinter import *

# Расшифровка ======================================================================
def goDecode():
    if (rBtn.get() == 0 or rBtn.get() == 1):   # Первые два вида расшифровки
        goCode()                               # идентичные как в шифровке
    else:
        tOutput.delete(1.0, END)
        tIn = tInput.get(1.0, END)
        tIn = tIn[0:len(tIn) - 1]              # Убираем перенос строки
        tOut = ""
        if (rBtn.get() == 2):                  # Увеличение кода символа на 1
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - 1)
        elif (rBtn.get() == 3):                # Смещение по коду циклически до 33
            p = 0
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - p)
                p = (p + 1) % 33
        tOutput.insert(1.0, tOut)

# Шифровка =========================================================================
def goCode():
    tOutput.delete(1.0, END)
    tIn = tInput.get(1.0, END)
    tIn = tIn[0:len(tIn) - 1]                   # Убираем перенос строки
    tOut = ""
    if (rBtn.get() == 0):                       # Инверсия ******** (Мир => риМ)
        for i in range(len(tIn) -1, -1, -1):   # Слово "мир" => (3-1, -1, -1) от 2 до -1 с шагом -1
            tOut += tIn[i]                      # Счётчик сработает 3 раза tIn[2], tIn[1], tIn[0]) "рим"

    elif (rBtn.get() ==  1):                    # Замена с соседней ********* (Привет => рПвите)
        for i in range(0, len(tIn) - 1, 2):     # Слово "Привет" => (0, 6-1, 2) от 0 до 5 с шагом 2 => "П и е "
                                                # Счётчик сработает 3 раза, но мы добавляем конкатенацию
            tOut += tIn[i + 1] + tIn[i]         # [0+1]+[0]=рП, [2+1]+[2]=ви, [4+1]+[4]=те. рП+ви+те = рПвите

    elif (rBtn.get() == 2):                     # Увеличение кода символа на 1 ******** (Мир => Нйс)
        for i in range(len(tIn)):               # Слово "Мир" счётчик сработает 3 раза (0, 1, 2)
            tOut += chr(ord(tIn[i]) + 1)        # ord("М")+1=1052+1, ord("и")+1=1080+1, ord("р")+1=1088+1,
                                                # chr(1053)=Н, chr(1081)=й, chr(1089)=с        => Нйс

    elif (rBtn.get() == 3):                     # Смещение по коду циклически до 33 ******* (Мир => Мйт)
        p = 0                                   # При каждом срабатывании счётчика будет увеличиваться на +1 до 33
        for i in range(len(tIn)):               # Счётчик сработает 3 раза при слове Мир
            tOut += chr(ord(tIn[i]) + p)        # ord("М")+0=1052, ord("и")+1=1080+1=1081, ord("р")+2=1088+2=1090
                                                # chr(1052)=М, chr(1081)=й, chr(1090)=т        => Мйт
            p = (p + 1) % 33                    # p=(0+1)%33=1%33=1, p=(1+1)%33=2%33=2, p=(2+1)%33=3%33=3
                                                # После того как доходим до 33 счётчик сбрасывается 33%33=0 => p=0
                                                # это произойдёт в том случае если слов больше 33

    tOutput.insert(1.0, tOut)                   # Возвращаем полученое значение в зависимости от выбранного метода

# Очистить текст =====================================================================
def clearText():
    tInput.delete(1.0, END)                     # Очищаем поле ввода
    tOutput.delete(1.0, END)                    # Очищаем поле вывода

# Результат -> Исходный ==============================================================
def resToDef():
    tInput.delete(1.0 , END)                    # Очищаем поле ввода
    txt = tOutput.get(1.0, END)                 # Берём поле вывода
    txt = txt[0:len(txt) - 1]                   # Убираем перенос строки
    tInput.insert(1.0, txt)                     # Заполняем поле ввода

# Вставить в исходный текст ==========================================================
def pasteFromClipboard():
    try:
        tInput.insert(END, root.clipboard_get())
    except:
        tInput.insert(END, "\nОшибка: буфер пуст")

# Копировать результат ===============================================================
def copyToClipboard():
    root.clipboard_clear();
    root.clipboard_append(tOutput.get(1.0, END))

# ====================================================================================
def setMenuPos(event):
    menuInput.post(event.x_root, event.y_root)

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
tInput.insert(1.0, """Введите здесь текст который хотите зашифровать""")

scrollInput = Scrollbar(command=tInput.yview, width=20)   # Переменная полосы прокрутки ввода
scrollInput.place(x=570, y=20, height=132)                # Позиция на экране полосы прокрутки ввода
tInput["yscrollcommand"] = scrollInput.set
# = = = = = = = = = = = = = = = = = = = = =
tOutput = Text(width=70, height=8, wrap=WORD)             # Размеры окна вывода
tOutput.place(x=5, y=180)                                 # Начало координат окна вывода
tOutput.insert(1.0, "Здесь появится шифр в зависимости от метода шифрования")

scrollOutput = Scrollbar(command=tOutput.yview, width=20) # Переменная полосы прокрутки вывода
scrollOutput.place(x=570, y=180, height=132)              # Позиция на экране полосы прокрутки вывода
tOutput["yscrollcommand"] = scrollOutput.set

# Меню на правую кнопку
menuInput = Menu(tearoff=False)
menuInput.add_command(label="Копировать результат", command=copyToClipboard)
menuInput.add_command(label="Вставить в исходный текст", command=pasteFromClipboard)
menuInput.add_command(label="Результат -> Исходный", command=resToDef)
menuInput.add_command(label="Очистить текст", command=clearText)
tInput.bind("<Button-3>", setMenuPos)  # Чтобы меню появлялось в окне ввода при нажатии правой кнопки мыши
tOutput.bind("<Button-3>", setMenuPos) # Чтобы меню появлялось в окне вывода при нажатии правой кнопки мыши

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

