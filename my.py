from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(150000)

def get_reward(a):
    d,r,u,t=defaultdict(list),[],set(),0
    for i,j in a:
        if i==j:
            t+=2
        else:
            d[i].append(j)
    def dfs(x,q):
        if x in q:
            r.append(q)
            u.update(q)
            return
        q.add(x)
        for i in d[x]:
            dfs(i,q)
    for i in d:
        if i not in u:
            dfs(i,set())
    return t+sum(2**len(i)*len(i) for i in r)

print(get_reward([(1,3), (4,6), (3,1), (6,7), (7,4), (8,8)]))