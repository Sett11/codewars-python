def spiralize(size):
    pass

#print(spiralize(5))

def solve(n):
    f=lambda x:sum(map(int,str(x)))
    m,i,d=f(n),1,{}
    while n>0:
        m=max(f(n),m)
        if m not in d:
            d[m]=n
        n=n-(n%(10)**i)-1
        i+=1
    return d[m]

print(solve(48))