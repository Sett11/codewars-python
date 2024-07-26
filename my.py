def calc_rot_time(a):
    n,m,u,c=len(a),len(a[0]),set(sum(a,[])),0
    f=lambda i,j,w:[(k,p) for k,p in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if k>=0 and k<n and p>=0 and p<m and a[k][p]==w]
    if len(u)==1:
        if 2 in u:
            return c
        return -1
    while len(u)>1 and 2 in u:
        t=[]
        for i in range(n):
            for j in range(m):
                if a[i][j]==2:
                    t.extend(f(i,j,1))
                if a[i][j]==1:
                    l=len(f(i,j,0))
                    if [i,j] in [[n-1,m-1],[0,n-1],[0,0],[0,m-1]] and l==2:
                        return -1
                    if (i in [0,n-1] or j in [0,m-1]) and l==3:
                        return -1
                    if l==4:
                        return -1
        for i,j in t:
            a[i][j]=2
        u=set(sum(a,[]))
        if not t and len(u)>1 and 2 in u:
            return c
        c+=1
    return c
            

print(calc_rot_time([[2,1,1],
                     [1,1,1]]))