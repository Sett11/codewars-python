import math

def p(x):
    if(x<2):
        return False
    if(x==2):
        return True
    c=2
    while c<=math.sqrt(x):
        if(x%c==0):
            return False
        c+=1
    return True

def f(l,n):
    c=l[-1:][0]+1
    while c<=n:
        if(p(c)):
            l.append(c)
        c+=1
    return l

def s(l,n):
    return [[i,j] for i in l for j in l if i+j==n and i<=j]

def goldbach(n,a=[2,3,5,7,11,13,17]):
    if(a[-1:][0]>=n):
        s(a,n)
    return s(f(a,n),n)

print(goldbach(3448))
print(goldbach(6))