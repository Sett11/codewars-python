zero,one=0,1

def multiply(n,m):
    t=zero
    k=one+one
    while n:
        if n&one:
            t+=m
        m<<=one
        n>>=one
    return t

print(multiply(2,7))