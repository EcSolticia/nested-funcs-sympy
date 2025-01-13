import sys
import sympy
from sympy import *

x = symbols('x')

t = sin(x)

def iterate(f, x, f_0):
    try:
        return f.subs(x, f_0)
    except:
        print("Something went wrong in iterate(f, x, f_0)")

def nest(f_0, x, n):
    f = f_0
    for i in range(n - 1):
        f = iterate(f, x, f_0)
    return f

nested = nest(t, x, 10)
print(nested)