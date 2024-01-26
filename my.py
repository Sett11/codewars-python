def magical_well(a,b,n):
    r=0
    while n:
        r+=a*b
        b+=1
        a+=1
        n-=1
    return r

print(magical_well(6,5,3))