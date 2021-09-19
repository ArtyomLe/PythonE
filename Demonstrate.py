# =========================================================================================
from tkinter import *
from tkinter import ttk

root = Tk()


WIDTH = 1024  # Ширина окна программы
HEIGHT = 600  # Высота окна программы


POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2   # Координаты размещения окна по центру
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2 # Координаты размещения окна по центру

root.title("ניסוי")                                  # Устанавливаем заголовок
root.resizable(False, False)                         # Запрещаем изменять размеры окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")   # Задаём позицию окна на эране


# ==========================================================================================

cmbx = ttk.Combobox(root)           # Задаём переменую для виджета(cmbx)
cmbx["state"] = "readonly"          # Настраиваем её состояние только для чтения
cmbx.place(x=60, y=50)              # Выводим с помощью метода .place
cmbxSelect = StringVar()            # Создаём переменую куда виджет будет помещать выбранное значение
cmbx["textvariable"] = cmbxSelect   # Привязываем переменную к Combobox

# Создаём список значений и передаём его в Combobox
cmbx["values"] = ["Привет", "Как дела?", "Это тоже надпись", "Ещё одно значение"]
cmbx.current(0) # Устанавливаем активный выбор (в данном случае "Привет") можно и без

# Назначаем метод который будет вызываться при выборе какого либо значения 
def showInTerminal(*args):
    lbl["text"] = cmbxSelect.get() # берёт значения из списка

cmbx.bind("<<ComboboxSelected>>", showInTerminal)

lbl = Label(root, font="Arial 15")
lbl["text"] = "Здесь выбор"
lbl.place(x=10, y=10)

root.mainloop()