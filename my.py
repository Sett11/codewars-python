def lucasnum(n):
    k=abs(n)
    a,b=2,1
    while k:
        a,b=b,a+b
        k-=1
    return -a if n<0 and n&1 else a