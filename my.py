def f(n,b):
    a,r='01',''
    while n:
        r=a[n%b]+r
        n//=2
    return r

def z(s):
    a=list(range(len(s)))[::-1]
    return sum([(1 if j=='1' else 0)*2**a[i] for i,j in enumerate(s)])

def add(a,b):
    return f(z(a)+z(b),2) or '0'


print(add('111','10'))