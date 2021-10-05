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

root.mainloop()

