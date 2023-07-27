def moving_particles(a):
    i,l,k=0,len(a),[i for i,j in enumerate(a) if j>0]
    if (k and not [j for j in a[k[0]+1:] if j<0]) or not k:
        return a
    while i<l-1:
        if a[i]>0 and a[i+1]<0:
            b,c=abs(a[i]),abs(a[i+1])
            t=b+c
            t=t if b>=c else -t
            a[i+1]=t
            a=a[:i]+a[i+1:]
            l-=1
            i-=1
        i+=1
    return moving_particles(a)

print(moving_particles([-1, 3, -1, 2]))
print(moving_particles([3,-1]))
print(moving_particles([5, -1, -2, -9]))
print(moving_particles([-2, 8, -10, 2, 4, 4, 4, -9]))
print(moving_particles([9, 9, -9, -6, -4, -2, 8, 4, 9]))