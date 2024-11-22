from itertools import product as p

def cockroaches(a):
    n,m,r,q=len(a),len(a[0]),[0]*10,{}
    l=list(p(range(n),[0]))[:-1]+list(p([n-1],range(m)))[:-1]+list(p(range(n-1,-1,-1),[m-1]))[:-1]+list(p([0],reversed(range(m))))[:-1]
    g=next(i for i,j in enumerate(l) if a[j[0]][j[1]].isdigit())
    l=(l[g:]+l[:g])[::-1]
    i,j=l.pop()
    c=int(a[i][j])
    q[(i,j)]=c
    for i,j in l:
        if a[i][j].isdigit():
            c=int(a[i][j])
        q[(i,j)]=c
    for i in range(1,n-1):
        for j in range(1,m-1):
            t=a[i][j]
            if t!=' ':
                if t=='U':
                    r[q[(0,j)]]+=1
                elif t=='D':
                    r[q[(n-1,j)]]+=1
                elif t=='L':
                    r[q[(i,0)]]+=1
                else:
                    r[q[(i,m-1)]]+=1
    return r

print(cockroaches(['123', '8U4', '765']))