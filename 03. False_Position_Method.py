print("Name: Md. Abdur Rouf Id: 173462059")
import math
I=100
def f(eqn,x):
    return eval(eqn)

equation=input("Enter the equation of f(x)=")
a= float(input("Enter the value of a:"))
b= float (input("Enter the value of b:"))

def regulaFalsi(a,b):
    if(f(equation,a) * f(equation,b)>=0):
        print("No Root")
        return
    c=a
    for i in range (I):
        c=(a*f(equation,b) - b*f(equation,a)) / (f(equation,b) - f(equation,a))
        if f(equation,c)==0:
            break
        elif f(equation,a) * f(equation,c)<0:
            b=c
        else:
            a=c
    print("The root:","%.4f" %c)

regulaFalsi(a,b)
