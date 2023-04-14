def array_change(a):
    i=0;c=a.copy()
    while i<len(a)-1:
        if(a[i]>=a[i+1]):
            a[i+1]=a[i]+1
        i+=1
    return sum(a)-sum(c)

print(array_change([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]))