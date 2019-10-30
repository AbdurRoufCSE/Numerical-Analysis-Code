print("Name: Md. Abdur Rouf Id: 173462059")
def d(x,y):
    return (x+y)
def rK(x0,y0,h):

    n=1

    y=y0
    for i in range(1,n+1):
        k1=h*d(x0,y0)
        k2=h*d(x0+0.5*h,y+0.5*k1)
        k3=h*d(x0+0.5*h,y+0.5*k2)
        k4=h*d(x0+h,y+k3)

        y=y+(1/6)*(k1+2*k2+2*k3+k4)

        x0 =x0+h
    return y

x0=0
y=1
h=0.1
print("The value of y at x is:","%.6f"%rK(x0,y,h))