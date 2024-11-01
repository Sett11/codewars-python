def wheat_from_chaff(a):
    b=[i for i,j in enumerate(a) if j<0]
    for i in range(len(a)):
        if a[i]>0 and b:
            x=b.pop()
            if x>i:
                a[i],a[x]=a[x],a[i]
    return a

print(wheat_from_chaff([-3,4,-10,2,-6]))
print(wheat_from_chaff([8,10,-6,-7,9]))