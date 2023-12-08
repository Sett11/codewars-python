def count_find_num(a,n):
    l=len(a)
    if l==2:
        r=sorted(a[0]**i*a[1]**j for i in range(1,16) for j in range(1,16))
    if l==3:
        r=sorted(a[0]**i*a[1]**j*a[2]**k for i in range(1,16) for j in range(1,16) for k in range(1,16))
    if l==4:
        r=sorted(a[0]**i*a[1]**j*a[2]**k*a[3]**v for i in range(1,16) for j in range(1,16) for k in range(1,16) for v in range(1,16))
    if l==5:
        r=sorted(a[0]**i*a[1]**j*a[2]**k*a[3]**v*a[4]**c for i in range(1,16) for j in range(1,16) for k in range(1,16) for v in range(1,16) for c in range(1,16))
    r=list(filter(lambda x:x<=n,r))
    return [len(r),r[-1]] if r else []

print(count_find_num([2, 29, 37, 73],6850316))