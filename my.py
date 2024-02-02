from functools import cache

@cache
def recaman(n):
    s,r=set([0]),[0]
    while len(r)<=n:
        t=r[-1]-len(r)
        if t>0 and t not in s:
            r.append(t)
            s.add(t)
        else:
            t=r[-1]+len(r)
            r.append(t)
            s.add(t)
    return r[n]

print(recaman(11))