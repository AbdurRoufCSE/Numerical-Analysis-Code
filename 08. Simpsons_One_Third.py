print("Name: Md. Abdur Rouf Id: 173462059")
import math
def func(eqn, x):
    return eval(eqn)
F = input("Input Equation f(x)= ")

def SimpSons(l, u, n):
    h = (u - l) / n
    x = list()
    y = list()

    i = 0
    while i <= n:
        x.append(l + i * h)
        y.append(func(F, x[i]))
        i += 1

    r = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            r += y[i]
        elif i % 2 != 0:
            r += 4 * y[i]
        else:
            r += 2 * y[i]
        i += 1
    r = r * (h / 3)
    return r


l = int(input("Lower Limit: "))
u = int(input("Upper Limit: "))
n = int(input("Interval Iteration: "))
print("The Result: %.6f" % SimpSons(l, u, n))
