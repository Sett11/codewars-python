def construct_graph(a):
    if not a:
        return [['+']]
    if len(a)==1 and a[0]['x']==0 and a[0]['y']==0:
        return [['*']]
    a=[tuple(i.values()) for i in a]
    x,y=[i for i in zip(*a)]
    r,u=[[(j,i) for j in range(min(0,min(x)),max(max(x),abs(max(x)))+1)] for i in range(min(0,min(y)),max(abs(max(y)),max(y))+1)][::-1],set(a)
    n,m=len(r),len(r[0])
    for i in range(n):
        for j in range(m):
            if r[i][j]==(0,0):
                k=p=0
                while k<n:
                    if r[k][j] not in u and r[k][j]!='*':
                        r[k][j]='|'
                    k+=1
                while p<m:
                    if r[i][p] not in u and r[i][p]!='*':
                        r[i][p]='-'
                    p+=1
                if r[i][j] not in u:
                    r[i][j]='+'
            if r[i][j] in u:
                r[i][j]='*'
            if r[i][j] not in u and isinstance(r[i][j],tuple):
                r[i][j]=' '
    while '*' not in r[0] and '+' not in r[0]:
        r.pop(0)
    q=[i for i in zip(*r)]
    for i in range(len(q)-1,-1,-1):
        if '*' in q[i] or '+' in q[i]:
            break
    return [j[:i+1] for j in r]



print(*construct_graph([{'x': 0, 'y': 3}]),sep='\n')
print(*construct_graph([{"x": -2, "y": -3}, {"x": 1, "y": -3}]),sep='\n')
print(*construct_graph([
                {"x":  1, "y":  1},
                {"x":  3, "y":  2}
            ]),sep='\n')