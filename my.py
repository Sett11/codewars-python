def alternate_sort(l):
    a=sorted(list(filter(lambda e:e>=0,l)))
    b=sorted(list(filter(lambda e:e<0,l)),reverse=True)
    c=[]
    while len(a) or len(b):
        if(len(b)):c.append(b.pop(0))
        if(len(a)):c.append(a.pop(0))
    return c

print(alternate_sort([5, -42, 2, -3, -4, 8, -9,]))