import sys
from sympy import symbols, sin

#initialize x as a sympy symbol
x = symbols('x')

#apparently "normal" sine function
f_0 = sin(x)
f = f_0

n = int(input()) #number of interations
if (n == 0): sys.exit()

for i in range(n - 1):
    f = f.subs(x, f_0)

# fails from around n = 245 to n = 249 and above due to hitting maximum recursion limit
print(f)