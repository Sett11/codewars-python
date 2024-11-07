def connect_the_dots(s):
    a=[list(i) for i in s.splitlines()]
    b=[i[1:] for i in sorted(sum([[(ord(p)-97,i,j) for j,p in enumerate(k) if p!=' '] for i,k in enumerate(a)],[]))]
    def dfs(i,j,k,p):
        a[i][j]='*'
        if (i,j)==(k,p):
            return
        elif i==k:
            if j<p:
                dfs(i,j+1,k,p)
            else:
                dfs(i,j-1,k,p)
        elif j==p:
            if i<k:
                dfs(i+1,j,k,p)
            else:
                dfs(i-1,j,k,p)
        elif i<k and j<p:
            dfs(i+1,j+1,k,p)
        elif i>k and j>p:
            dfs(i-1,j-1,k,p)
        elif i<k and j>p:
            dfs(i+1,j-1,k,p)
        else:
            dfs(i-1,j+1,k,p)
    t=b.pop(0)
    while b:
        dfs(*t,*b[0])
        t=b.pop(0)
    return '\n'.join(''.join(i) for i in a)+'\n'

print(connect_the_dots((
            "           \n" +
            " a       b \n" +
            " e         \n" +
            "           \n" +
            " d       c \n" +
            "           \n" ))) 