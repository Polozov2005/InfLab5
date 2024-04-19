### Проведение расчётов
import numpy as np
import sympy as sy

# Задание функции
def f(x):
    global A, alpha, m
    return A * np.e**(-alpha * (x - m))

# Поиск определённого интеграла
def solve():
    global x_min, x_max, A, alpha, m
    x = sy.Symbol("x")
    solve = sy.integrate(f(x), (x, x_min, x_max))
    return solve

### Построение графика
import matplotlib.pyplot as plt
import locale
def plotting():
    global x_min, x_max, A, alpha, m

    # Настройки графика
    fig, ax = plt.subplots()
    locale.setlocale(locale.LC_NUMERIC, "de_RU")
    font = {'family': font_root,
            'size': fontsize_root}
    plt.rc('font', **font)
    ax.ticklabel_format(useLocale=True)
    ax.grid(linewidth = 0.5, color='#7b7b7b')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    # Настройка офомления графика
    ax_color = foreground_root
    ax.set_facecolor(background_root)
    fig.set_facecolor(background_root)
    ax.spines['bottom'].set_color(ax_color)
    ax.spines['left'].set_color(ax_color) 
    ax.tick_params(axis='x', colors=ax_color)
    ax.tick_params(axis='y', colors=ax_color)

    # Постройка графика
    x = np.linspace(x_min, x_max, 1000)
    ax.plot(x, f(x), color=bluecolor)

    # Откладывание интеграла в виде пунктирной прямой
    y = solve() + x*0
    ax.plot(x, y, '--', color=bluecolor)

    plt.ylim(0)

    # Сохранение файла
    fig.set_size_inches(7.2, 7.2)
    fig.savefig('graph.png', dpi=100)

### Создание интерфейса
from tkinter import *
from tkinter import ttk
import re
# Костыль для того, чтобы интерфейс не был размытым
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# Создание окна программы
root = Tk()
root.title("Калькулятор")
root.geometry("1080x720")
root.resizable(False, False)
root.attributes("-toolwindow", True)

# Настройка оформления окна
background_root = '#181818'
foreground_root = '#cccccc'
bluecolor = '#4a9cd6'
fontsize_root = 16
font_root = 'Arial'
root.configure(bg=background_root)

# Настройка веса столбцов, т. е. какую часть окна занимает каждый столбец
root.columnconfigure(index=0, weight=4)
for column in range(1, 2+1): root.columnconfigure(index=column, weight=1)

# Вывод графика
initial_graph = PhotoImage(file="initial_graph.png")
canvas_graph = Canvas(width=720, height=720, background=background_root, highlightthickness=0)
canvas_graph.create_image(360, 360, image=initial_graph)
canvas_graph.grid(row=0, column=0, rowspan=8)

# Вывод интеграла
label_integral = ttk.Label(text='Интеграл')
label_integral.grid(row=0, column=1, columnspan=2)

## Ввод параметров
# Задание валидации
def is_valid(newval):
    return re.match("^[-]?\d*[.,]?\d*$", newval) is not None
check = (root.register(is_valid), "%P")

# Настройка оформления полей ввода
font_entry = 'Arial'
fontsize_entry = fontsize_root
background_entry = '#1f1f1f'
foreground_entry = foreground_root
insertbackground_entry = foreground_entry
highlightthickness_entry = 0
border_entry = 0
width_entry = 12

# A
label_A = ttk.Label(text="A")
label_A.grid(row=1, column=1)
entry_A = Entry(validate="key", 
                validatecommand=check,
                background=background_entry,
                insertbackground=insertbackground_entry,
                foreground=foreground_entry,
                highlightthickness=highlightthickness_entry,
                border=border_entry,
                font=(font_entry, fontsize_entry, 'bold'),
                width=width_entry
                )
entry_A.insert(0, "1")
entry_A.grid(row=1, column=2)

# alpha
label_alpha = ttk.Label(text="alpha")
label_alpha.grid(row=2, column=1)
entry_alpha = Entry(validate="key", 
                    validatecommand=check,
                    background=background_entry,
                    insertbackground=insertbackground_entry,
                    foreground=foreground_entry,
                    highlightthickness=highlightthickness_entry,
                    border=border_entry,
                    font=(font_entry, fontsize_entry, 'bold'),
                    width=width_entry
                    )
entry_alpha.insert(0, "-1")
entry_alpha.grid(row=2, column=2)

# m
label_m = ttk.Label(text="m")
label_m.grid(row=3, column=1)
entry_m = Entry(validate="key", 
                validatecommand=check,
                background=background_entry,
                insertbackground=insertbackground_entry,
                foreground=foreground_entry,
                highlightthickness=highlightthickness_entry,
                border=border_entry,
                font=(font_entry, fontsize_entry, 'bold'),
                width=width_entry
                )
entry_m.insert(0, "0")
entry_m.grid(row=3, column=2)

# x_min
label_x_min = ttk.Label(text="x_min")
label_x_min.grid(row=4, column=1)
entry_x_min = Entry(validate="key", 
                    validatecommand=check,
                    background=background_entry,
                    insertbackground=insertbackground_entry,
                    foreground=foreground_entry,
                    highlightthickness=highlightthickness_entry,
                    border=border_entry,
                    font=(font_entry, fontsize_entry, 'bold'),
                    width=width_entry
                    )
entry_x_min.insert(0, "0")
entry_x_min.grid(row=4, column=2)

# x_max
label_x_max = ttk.Label(text="x_max")
label_x_max.grid(row=5, column=1)
entry_x_max = Entry(validate="key", 
                    validatecommand=check,
                    background=background_entry,
                    insertbackground=insertbackground_entry,
                    foreground=foreground_entry,
                    highlightthickness=highlightthickness_entry,
                    border=border_entry,
                    font=(font_entry, fontsize_entry, 'bold'),
                    width=width_entry
                    )
entry_x_max.insert(0, "1")
entry_x_max.grid(row=5, column=2)

## Вывод кнопок
# Для очищения полей ввода
def click_clear():
    entry_A.delete(0, END)
    entry_alpha.delete(0, END)
    entry_m.delete(0, END)
    entry_x_min.delete(0, END)
    entry_x_max.delete(0, END)
btn_clear = Button(text='C', 
                   command=click_clear,
                   background=bluecolor,
                   foreground=background_root,
                   activebackground=background_root,
                   activeforeground=bluecolor,                   
                   highlightthickness=0,
                   width=3,
                   height=1,
                   border=0,
                   cursor='hand2',
                   font=('Arial', 16, 'bold'),
                   relief=SUNKEN
                   )
btn_clear.grid(row=6, column=1)

# Для расчёта
def click_solve():
    global x_min, x_max, A, alpha, m, graph
    A = float(entry_A.get())
    alpha = float(entry_alpha.get())
    m = float(entry_m.get())
    x_min = float(entry_x_min.get())
    x_max = float(entry_x_max.get())
    label_solve["text"] = solve()
    plotting()
    graph = PhotoImage(file="graph.png")
    canvas_graph.create_image(360, 360, image=graph),
btn_solve = Button(text="Результат",
                   command=click_solve,
                   background=bluecolor,
                   foreground=background_root,
                   activebackground=background_root,
                   activeforeground=bluecolor,
                   highlightthickness=0,
                   width=10,
                   height=1,
                   border=0,
                   cursor='hand2',
                   font=('Arial', 16, 'bold'),
                   relief=SUNKEN
                   )
btn_solve.grid(row=6, column=2)

# Вывод результата
label_solve = Label(
    text="Ответ",
    background=background_root,
    foreground=bluecolor,
    highlightbackground=bluecolor,
    highlightthickness=2,
    height=2,
    width=16,
    font=(font_root, fontsize_root, 'bold')
    )
label_solve.grid(row=7, column=1, columnspan=2)

# Вывод окна
root.mainloop()