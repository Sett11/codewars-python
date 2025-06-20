from collections import defaultdict
from itertools import combinations_with_replacement

def add_spaces(s):
    if '0' not in s:
        return ' '.join(list(s))
    n, l = 50, len(s)
    while n > 9:
        if len(''.join(map(str, range(10, n+1)))) == l - 9:
            break
        n -= 1
    r, g, q, u = [], defaultdict(set), '1234567890', set(s[:i] for i in range(1, l+1))
    nums = set([j for j in sum([[''.join(i), ''.join(i[::-1])] for  i in combinations_with_replacement(q,2)], []) + [i for i in q if i != '0'] + ['10'] if int(j) <= n and j[0] != '0'])
    for i in nums:
        for j in nums:
            if i != j:
                g[i].add(j)
                g[j].add(i)
    def dfs(e, a, w):
        if len((x:=''.join(a))) > l or x not in u or r:
            return
        if ''.join(a) == s:
            r.append(' '.join(a))
            return
        for i in g[e]:
            if ''.join(a + [i]) in u and i not in w:
                nw = w.copy()
                nw.add(i)
                dfs(i, a + [i], nw)
    dfs(s[0], [s[0]], set([s[0]])), dfs(s[:2],[s[:2]], set([s[:2]]))
    return r[0] if r else s


print(add_spaces('206513188102221121415143923241619171127'))
print(add_spaces('147113917185411610816122315'))
print(add_spaces('121110987654312'))