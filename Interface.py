# Костыль, чтобы интерфейс не был размытым
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *
from tkinter import ttk

# Создание окна программы
root = Tk()
root.title("Калькулятор")
root.geometry("1080x720")

# Вывод графика
label_graph = ttk.Label(text="График функции")
label_graph.grid(row=0, column=0)

# Вывод интеграла
label_integral = ttk.Label(text='Интеграл')
label_integral.grid(row=0, column=1, columnspan=2)

# Вывод сообщения об ошибке
label_errmsg = ttk.Label(text="Ошибка")
label_errmsg.grid(row=1, column=1, columnspan=2)

## Ввод параметров
# A
label_A = ttk.Label(text="A")
label_A.grid(row=2, column=1)
entry_A = ttk.Entry()
entry_A.grid(row=2, column=2)

# alpha
label_alpha = ttk.Label(text="alpha")
label_alpha.grid(row=3, column=1)
entry_alpha = ttk.Entry()
entry_alpha.grid(row=3, column=2)

# m
label_m = ttk.Label(text="m")
label_m.grid(row=4, column=1)
entry_m = ttk.Entry()
entry_m.grid(row=4, column=2)

# x_min
label_x_min = ttk.Label(text="x_min")
label_x_min.grid(row=5, column=1)
entry_x_min = ttk.Entry()
entry_x_min.grid(row=5, column=2)

# x_max
label_x_max = ttk.Label(text="x_max")
label_x_max.grid(row=6, column=1)
entry_x_max = ttk.Entry()
entry_x_max.grid(row=6, column=2)

## Вывод кнопок
# Для очищения полей ввода
btn_clear = ttk.Button(text='C')
btn_clear.grid(row=7, column=1)

# Для расчёта
btn_solve = ttk.Button(text="Результат")
btn_solve.grid(row=7, column=2)

# Вывод результата
label_solve = ttk.Label(text="Результат")
label_solve.grid(row=8, column=1, columnspan=2)

# Вывод окна
root.mainloop()