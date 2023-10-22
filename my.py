def branch(n):
    c=1
    r=[]
    while c**2<n:
        c+=2
        r.append(c)
    if not r:
        return 0
    a=[i for i in range((r[-2] if len(r)>1 else 1)**2+1,r[-1]**2+1)]
    l=len(a)//4
    a=[a[i:i+l] for i in range(0,len(a),l)] if n>9 else [[2,3],[4,5],[6,7],[8,9]]
    for i in range(len(a)):
        if n in a[i]:
            return i

print(branch(8))