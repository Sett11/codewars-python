def moving_average(a,n):
    if(n<1):return None
    i=0;r=[]
    while i<=len(a)-n:
        r.append(sum(a[slice(i,i+n)])/n)
        i+=1
    return r if r else None

print(moving_average([40, 30, 50, 46, 39, 44],4))