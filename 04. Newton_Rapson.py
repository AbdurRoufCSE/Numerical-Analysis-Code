print("Name: Md. Abdur Rouf Id: 173462059")
def f(e, x):
    return eval(e)
F=input("Enter the f(x)=")
a = float(input("Enter the value of a:"))

def df(e1, x):
    return eval(e1)


F1 = input("df(x)=")


def newRap(x):
    h = f(F, x) / df(F1, x)
    while abs(h) >= 0.0001:
        h = f(F, x) / df(F1, x)
        x = x - h
    print("The root =", "%.4f" % x)


newRap(a)