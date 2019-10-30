print("Name: Md. Abdur Rouf Id: 173462059")
def u_cal(u,n):
    temp = u;
    for i in range(1,n):
        temp = temp*(u-i)
    return temp
def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f
n=5
x=[40,50,60,70,80]

y=[[0 for i in range(n)]
      for j in range(n)]
y[0][0]=31
y[1][0]=73
y[2][0]=124
y[3][0]=159
y[4][0]=190

#difference table
for i in range(1,n):
    for j in range(n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]
for i in range(n):
    print(x[i],end="\t")
    for j in range(n-i):
        print(y[i][j], end="\t")
    print("")


value=int(input("Enter the value:"))
sum=y[0][0]
u=(value-x[0])/(x[1]-x[0])

for i in range(1,n):
    sum = sum +(u_cal(u,i)*y[0][1])/fact(i)

print("Value at", value, "is",round(sum,6))


