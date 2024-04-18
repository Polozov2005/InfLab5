import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import locale

# Задание функции
def f(x):
    global A, alpha, m
    return A * np.e**(-alpha * (x - m))

# Поиск определённого интеграл
def solve():
    global x_min, x_max
    x = sy.Symbol("x")
    solve = sy.integrate(f(x), (x, x_min, x_max))
    return solve

A = 1
alpha = -1
m = 0

x_min = 0
x_max = 1



print(solve())

# Настройки графика
fig, ax = plt.subplots()
locale.setlocale(locale.LC_NUMERIC, "de_RU")
font = {'family': 'Times New Roman',
        'size': 12}
plt.rc('font', **font)
ax.ticklabel_format(useLocale=True)
ax.grid(linewidth = 0.3)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()

x = np.linspace(x_min, x_max, 1000)
ax.plot(x, f(x))
plt.ylim(0)

fig.set_size_inches(7.2, 7.2)
fig.savefig('test2png.png', dpi=100)

plt.show()