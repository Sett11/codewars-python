from functools import lru_cache

@lru_cache
def f(x):
    if(x==1):
        return True
    a=set([x])
    while 1:
        x=sum([int(i)**2 for i in list(str(x))])
        if(x==1):
            return True
        if(x in a):
            return False
        a.add(x)

def right(a,n):
    l,r=0,len(a)
    while r-l>1:
        m=(l+r)//2
        if a[m]<=n:
            l=m
        else:
            r=m
    return r

def g(x,o=[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]):
    if(o[len(o)-1]>=x):
        return o[:right(o,x)]
    i=o[len(o)-1]+1
    while i<=x:
        if(f(i)):
            o.append(i)
        i+=1
    return o

def performant_numbers(n):
    return g(n)

print(performant_numbers(100000))
print(performant_numbers(10000))