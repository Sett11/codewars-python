def sort_by_exclusion(a):
    b,n=sorted(set(a)),len(a)
    d,r=[b.index(i) for i in a],[0]*n
    for i in range(n):
        m=0
        for j in range(i):
            if d[i]>d[j] and r[j]>m:
                m=r[j]
        r[i]=m+1
    return n-max(r)


print(sort_by_exclusion(["M","O","A"]))