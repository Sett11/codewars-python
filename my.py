def buy(x,a):        
    i=0
    while i<len(a):
        t=x-a[i]
        if t in a:
            j=a.index(t)
            if i!=j:
                return sorted([i,j])
        i+=1

print(buy(5,[5,2,3,4,5]))