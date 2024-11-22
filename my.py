def f(n,m):
    f=lambda x:x*(x+1)//2
    return f(m-1)*(n//m)+f(n%m)


print(f(15,10))
print(f(10,5))
print(f(20,20))
print(f(75159665, 69299369))