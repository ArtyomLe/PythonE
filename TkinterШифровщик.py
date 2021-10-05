from tkinter import *

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

btnDecode = Button(text="Дешифровать", width=25, command=godeCode) # Переменная для кнопки дешифрования справа вверху
btnDecode.place(x=600, y=50)                                       # позиция в окне

# Радиокнопки


root.mainloop()

