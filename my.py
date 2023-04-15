def calc(a):
    a=list(map(lambda e: e**2 if e>0 else e,a));i=0
    a.insert(0,0)
    while i<len(a):
        if(i%3==0):
            a[i]*=3
        if(i%5==0):
            a[i]*=-1
        i+=1
    return sum(a)

print(calc([ 1, -1, 10, -9, 16, 15, 45, -73, -26 ]))