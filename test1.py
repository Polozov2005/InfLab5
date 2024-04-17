import sympy as sy

def f(x):
    return 2**x

x = sy.Symbol("x")
solve = sy.integrate(f(x), (x, 1, 2))

print(solve)