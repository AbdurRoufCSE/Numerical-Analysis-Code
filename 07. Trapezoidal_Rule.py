print("Name: Md. Abdur Rouf Id: 173462059")
def y(eqn,x):
    return eval(eqn)
eqn = input("Input Equation f(x)= ")

def trap(a,b,n):
    h = (b - a) / n
    s = (y(eqn,a) + y(eqn,b))
    i = 1
    while i < n:
        s += 2 * y(eqn,a + i * h)
        i += 1
    return ((h / 2 ) * s)

x0 = int (input("Lower Limit: "))
xn = int (input("Upper Limit: "))
n = int (input("Iteration Number: "))

print("The Value Is : ", "%.4f" %trap (x0,xn,n))