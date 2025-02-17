def create_box(m,n):
    if m==1:
        return [[1]]*n
    a=[[1]+[0]*(m-2)+[1] for _ in range(n)]
    a[0]=[1]*m
    a[-1]=[1]*m
    def f(a):
        for i in range(1,n//2):
            for j in range(1,m//2):
                a[i][j]=min(a[i-1][j],a[i][j-1])+1
        return a
    a=f(a)
    a=f(a[::-1])
    a=f([i[::-1] for i in a[::-1]])
    a=f(a[::-1])
    k,q=m//2,n//2
    def ff(a):
        for i in range(1,n-1):
            if a[i][k]==0:
                if a[i][k-1]==a[i][k+1] and a[i-1][k]==a[i][k-1]-1:
                    a[i][k]=a[i][k-1]
        return a
    a=ff(a)
    a=ff(a[::-1])
    def fff(a):
        for i in range(1,m-1):
            if a[q][i]==0:
                if a[q-1][i]==a[q+1][i] and a[q][i-1]==a[q-1][i]-1:
                    a[q][i]=a[q-1][i]
        return a
    a=fff(a)
    a=fff([i[::-1] for i in a])
    w=max(sum(a,[]))+1
    for i in range(n):
        for j in range(m):
            if not a[i][j]:
                a[i][j]=w
    return a

print(create_box(1,5))
print(*create_box(5,8),sep='\n')
print(*create_box(10,9),sep='\n')