from itertools import product


def proc_seq(*a):
    r=set([int(''.join([str(k) for k in j])) for j in product(*[tuple(map(int,str(i))) for i in a]) if j[0]])
    q=[]
    b,c,d,e=len(r),min(r),max(r),sum(r)
    if b not in q:q.append(b)
    if c not in q:q.append(c)
    if d not in q:q.append(d)
    if e not in q:q.append(e)
    return q

print(proc_seq(22,22,22,22))