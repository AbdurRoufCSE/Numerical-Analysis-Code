print("Name: Md. Abdur Rouf Id: 173462059")
import math
def f(e,x):
    return eval(e)
F=input("f(x)=")
x1=float(input("Enter the value of x1="))
x2=float(input("Enter the value of x2="))

def secant(x1,x2):

    x3=x2-f(F,x2)*(x2-x1)/(f(F,x2)-f(F,x1))
    error=1
    while error>0.0001:
        x3 = x2 - f(F, x2) * (x2 - x1) / (f(F, x2) - f(F, x1))
        error=abs(x3-x2)/x3
        x1=x2
        x2=x3
    print("The root :","%.4f"%x3)
secant(x1,x2)