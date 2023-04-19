def least_larger(a,i):
    r=a[i]
    m=1000
    for e in a:
        if(e>r):
            m=min(m,e)
    return a.index(m) if m!=1000 else -1

print(least_larger([4, 1, 3, 5, 6],0))