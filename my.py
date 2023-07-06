def reduce_fraction(f):
    i,n=f[0]==max(f),600
    while n:
        t,m=max(f)/n,min(f)/n
        if t==int(t) and m==int(m):
            t,m=int(t),int(m)
            return (t if i else m,m if i else t)
        n-=1

print(reduce_fraction((60,20)))
print(reduce_fraction((80,120)))
print(reduce_fraction((10956590, 13611876)))