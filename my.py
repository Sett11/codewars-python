def is_bouncy(n):
    a=sorted(list(map(int,str(n))))
    b=sorted(a,reverse=True)
    c=list(map(int,str(n)))
    return c!=a and c!=b
print(is_bouncy(120))