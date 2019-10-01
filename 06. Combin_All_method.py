print("Name: Md. Abdur Rouf Id: 173462059")
import math
I=100
F=input("Enter the f(x)=")
a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))
print("1. Bisection method  press 1 \n"
      "2. False position method  press 2\n"
      "3. Newton rapson method  press 3 \n"
      "4. Secand method  press 4 \n")
key=int(input("Enter the choose one from the options : "))

if(key==1):
    def f(e,x):
        return eval(e)
    def bisection(a, b):
        if (f(F,a) * f(F,b) >= 0):
            print("No root")
            return
        c = a
        while ((b - a) >= 0.01):
            c = (a + b) / 2
            if (f(F,c) == 0.0):
                break
            if (f(F,c) * f(F,a) < 0):
                b = c
            else:
                a = c
        print("The root is:", "%.4f" % c)
    bisection(a, b)

elif(key==2):
    def f(e,x):
        return eval(e)


    def false_position(a, b):
        if (f(F,a) * f(F,b) >= 0):
            print("No root")
            return
        c = a
        for i in range(I):
            c = (a * f(F,b) - b * f(F,a)) / (f(F,b) - f(F,a))
            if (f(F,c) == 0):
                break
            if (f(F,a) * f(F,c) < 0):
                b = c
            else:
                a = c
        print("The root is :", "%.4f" % c)

    false_position(a, b)
elif(key==3):
    def f(e,x):
        return eval(e)
    def df(e1,x):
        return eval(e1)
    F1=input("df(x)=")
    def newRap(x):
        h=f(F,x)/df(F1,x)
        while abs(h)>=0.0001:
            h = f(F, x) / df(F1, x)
            x=x-h
        print("The root =","%.4f"%x)
    newRap(a)
elif(key==4):
    def f(e,x):
        return eval(e)
    def secant(x1,x2):

        x3=x2-((f(F,x2)*(x2-x1))/(f(F,x2)-f(F,x1)))
        error=1
        while error > 1e-4:
            x3 = x2 - ((f(F, x2) * (x2 - x1)) / (f(F, x2) - f(F, x1)))
            error=abs(x3-x2)/x2
            x1=x2
            x2=x3
        print("The root is =","%.4f"%x3)
    secant(a,b)



else:
    print("choose from the options ")