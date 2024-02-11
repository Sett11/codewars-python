def count(a,t,x):
    if x==0:
        return len([i for i in a if i==t])
    c=0
    for i in a:
        n=abs(i-t)
        if divmod(n,x)[1]==0:
            c+=1
    return c

print(count([-4,6,8],-7,-3))