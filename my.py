def loose_change(l,n):
    r=[i for i in l if n%i==0 and i!=1]
    if(len(r)):
        return n//max(r)
    l=l[::-1]
    c=0
    for i in range(len(l)):
        while n>=l[i]:
            n-=l[i]
            c+=1
    return c

print(loose_change([1, 5, 10, 25], 37))
print(loose_change([1, 4, 5, 10], 8))