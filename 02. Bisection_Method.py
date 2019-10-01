print("Name: Md. Abdur Rouf Id: 173462059")
def f(x):
    return x*x-2*x-3
def bisection(a,b):
    if(f(a)*f(b)>=0):
        print("No root ")
        return
    c=a
    while((b-a)>=0.01):
        c=(a+b)/2
        if(f(c)==0.0):
            break
        if(f(c)*f(a)<=0):
            b=c
        else:
            a=c
    print("The root is:","%.4f"%c)
a=2
b=3.2
bisection(a,b)
