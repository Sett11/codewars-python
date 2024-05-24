def bubble(a):
    n,r=len(a),[]
    for i in range(1,n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                t=a.copy()
                r.append(t)
    return r

print(bubble([2,1,4,3]))