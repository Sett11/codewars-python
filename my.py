def closest(a):
    m=float('Inf')
    a=list(set(a))
    for i in range(len(a)):
        t=abs(0-a[i])
        m=min(m,t)
        a[i]=[t,a[i]]
    a=[i[1] for i in a if i[0]==m]
    if len(a)==1:
        return a[0]


print(closest([2, 4, -1, -3]))
print(closest([5, 2, -2]))