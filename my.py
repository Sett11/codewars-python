def create_spiral(n):
    if type(n)!=int or n<1:
        return []
    a=list(range(1,n**2+1))
    r,a,k=[a[:n]],a[n:],n-1
    while a:
        v=2
        while v:
            r.append(a[:k])
            a=a[k:]
            v-=1
        k-=1
    q,w,i=['l','d','r','u'],[r.pop()],0
    while r:
        v=r.pop()
        if q[i%4]=='l':
            for j in range(len(w)-1,-1,-1):
                w[j].insert(0,v.pop(0))
        elif q[i%4]=='d':
            w.append(v[::-1])
        elif q[i%4]=='r':
            for j in range(len(w)-1,-1,-1):
                w[j].append(v.pop())
        else:
            w.insert(0,v)
        i+=1
    if n%2==0:
        w=[p[::-1] for p in w][::-1]
    return w

print(create_spiral(4))