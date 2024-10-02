def md(a,b):
    return [[sum(a[i][j]*b[j][k] for j in range(len(a))) for k in range(len(a[0]))] for i in range(len(a[0]))]

def multiply(a,b):
    c=md(a,b)
    for i in range(len(c)):
        for j in range(len(c[0])):
            a[i][j]=c[i][j]

def calc(m,n):
    a=[[1 if i==j else 0 for j in range(len(m[0]))] for i in range(len(m))]
    while n:
        if n&1:
            multiply(a, m)
        multiply(m, m)
        n>>=1
    return a

print(calc([[1,2], [0,1]],3))