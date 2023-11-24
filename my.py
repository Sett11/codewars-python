import math

def get_min(R,U):
    rm=(math.inf,'Z','Z')

    for v in U:
        rr=min(R,key=lambda x: x[0] if (x[1]==v or x[2]==v) and (x[1] not in U or x[2] not in U) else math.inf)
        if rm[0]>rr[0]:
            rm=rr
    
    return rm

def get_max(R,U):
    rm=(-math.inf,'Z','Z')

    for v in U:
        rr=max(R,key=lambda x:x[0] if (x[1]==v or x[2]==v) and (x[1] not in U or x[2] not in U) else -math.inf)
        if rm[0]<rr[0]:
            rm=rr

    return rm

def make_spanning_tree(a,m):
    n=math.inf if m=='min' else -math.inf
    a=([(n,'Z','Z')])+sorted([[i[1],i[0][0],i[0][1]] for i in a],key=lambda e:e[0],reverse=(True if m=='max' else False))
    s=list(set(''.join([i[1]+i[2] for i in a[1:]])))
    N=len(s)
    U={s[0]}
    T=[]

    while len(U)<N:
        r=get_min(a,U) if m=='min' else get_max(a,U)
        if r[0]==n:
            break
        T.append(r)
        U.add(r[1])
        U.add(r[2])

    return [(i[1]+i[2],i[0]) for i in T]


print(make_spanning_tree([
            ('AB', 1), ('AE', 1), ('BA', 1), ('EA', 1), ('GH', 1), ('HG', 1), ('AF', 2), ('DE', 2),
            ('DH', 2), ('ED', 2), ('FG', 2), ('FA', 2), ('GF', 2), ('HD', 2), ('BE', 3), ('CD', 3),
            ('DC', 3), ('EB', 3), ('DG', 4), ('EF', 4), ('FE', 4), ('GD', 4), ('AH', 5), ('BF', 5),
            ('FB', 5), ('HA', 5), ('BC', 6), ('CB', 6), ('CH', 7), ('HC', 7), ('CG', 8), ('GC', 8)
        ],'max'))