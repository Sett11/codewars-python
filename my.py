from functools import reduce
from collections import Counter

def id_best_users(*args):
    a,r=dict(zip(reduce(lambda a,c:set(a)&set(c),args),[0]*1000)),{}
    for i in args:
        t=Counter(i)
        for j in t:
            if j in a:
                a[j]+=t[j]
    for i,j in a.items():
        if j not in r:
            r[j]=[]
        r[j].append(i)
    return sorted([[i,sorted(r[i])] for i in r],reverse=True)

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
print(id_best_users(a1,a2,a3))