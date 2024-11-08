from functools import reduce

CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def f(n,b):
    a,r=CHARS[:b],''
    while n:
        r=a[n%b]+r
        n//=b
    return r

def ff(s,b):
    r=CHARS[:b]
    return str(reduce(lambda a,c:a*b+r.index(c),s,0))

def is_polydivisible(s,b):
    for i in range(1,len(s)+1):
        if int(ff(s[:i],b))%i:
            return False
    return True

def get_polydivisible(n,b):
    c=i=r=0
    while c<int(n):
        if is_polydivisible(f(i,b),b):
            c+=1
            r=f(i,b)
        i+=1
    return r or '0'

print(get_polydivisible('42',16))