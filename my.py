def distribution_of(a):
    r,i=[0,0],0
    while a:
        m=max(a[0],a[-1])
        r[i%2]+=m
        if m==a[0]:
            a=a[1:]
        else:
            a=a[:-1]
        i+=1
    return r


print(distribution_of([4,7,2,9,5,2]))
print(distribution_of([10,1000,2,1]))