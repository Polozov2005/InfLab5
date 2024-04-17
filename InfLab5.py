import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

def f(x):
    global A, alpha, m
    return A * np.e**(-alpha * (x - m))

A = 1
alpha = -1
m = 0

x_min = 0
x_max = 1

x = sy.Symbol("x")
solve = sy.integrate(f(x), (x, x_min, x_max))

print(solve)

x = np.linspace(-10, 10, 1000)
plt.plot(x, f(x))

plt.show()