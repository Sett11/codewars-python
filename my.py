d={0:0}

def recaman(n):
    k=0
    s,r=set([0]),[0]
    while len(r)<n:
        t=r[-1]-len(r)
        if t>0 and t not in s:
            r.append(t)
            s.add(t)
        else:
            t=r[-1]+len(r)
            r.append(t)
            s.add(t)
        k+=r[-1]
        d[len(r)]=k
    return d

recaman(2500000)

def rec(n):
    return d.get(n,0)

print(rec(200))