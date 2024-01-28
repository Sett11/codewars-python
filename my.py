def light_bulbs(a,n):
    while n:
        b=a.copy()
        for i in range(len(a)):
            if a[i-1]:
                b[i]=1 if b[i]==0 else 0
        a=b
        n-=1
    return a

print(light_bulbs([0,1,1,0,1,1],2))