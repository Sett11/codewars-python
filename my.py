def round_robin(a,t,n):
    i,s=0,0
    while 1:
        s+=t if t<=a[i] else a[i]
        a[i]-=t if t<a[i] else a[i]
        if a[i]==0 and i==n:
            return s
        i+=1
        if i>=len(a):
            i=0

print(round_robin([19, 17, 18, 5, 2, 1], 12, 2))