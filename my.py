def smallest(n):
    a,d=list(str(n)),{}
    l,m=len(a),n
    for i in range(l):
        b=a.copy()
        x=b.pop(i)
        for j in range(l):
            k=int(''.join(b[:j]+[x]+b[j:]))
            m=min(m,k)
            if k not in d:
                d[k]=[]
            d[k].append([i,j])
    return [m,*sorted(d[m],key=lambda x:(x[0],x[1]))[0]]

print(smallest(261235))