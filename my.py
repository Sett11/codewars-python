q=[1,-1]

def bishop(a,i,j):
    n,m=len(a),len(a[0])
    k,p=i,j
    while k>=0 and p>=0:
        if not a[k][p]:
            a[k][p]='&'
        k-=1
        p-=1
        if k>=0 and p>=0 and a[k][p] in q:
            break
    k,p=i,j
    while k<n and p<m:
        if not a[k][p]:
            a[k][p]='&'
        k+=1
        p+=1
        if k<n and p<m and a[k][p] in q:
            break
    k,p=i,j
    while k>=0 and p<m:
        if not a[k][p]:
            a[k][p]='&'
        k-=1
        p+=1
        if k>=0 and p<m and a[k][p] in q:
            break
    k,p=i,j
    while k<n and p>=0:
        if not a[k][p]:
            a[k][p]='&'
        k+=1
        p-=1
        if k<n and p>=0 and a[k][p] in q:
            break
    return a

def rook(a,i,j):
    n,m=len(a),len(a[0])
    k=i
    while k>=0:
        if not a[k][j]:
            a[k][j]='&'
        k-=1
        if k<n and a[k][j] in q:
            break
    k=i
    while k<n:
        if not a[k][j]:
            a[k][j]='&'
        k+=1
        if k<n and a[k][j] in q:
            break
    p=j
    while p>=0:
        if not a[i][p]:
            a[i][p]='&'
        p-=1
        if p>=0 and a[i][p] in q:
            break
    p=j
    while p<m:
        if not a[i][p]:
            a[i][p]='&'
        p+=1
        if p<m and a[i][p] in q:
            break
    return a

def bishops_and_rooks(a):
    n,m=len(a),len(a[0])
    for i in range(n):
        for j in range(m):
            if a[i][j] in q:
                if a[i][j]==-1:
                    a=bishop(a,i,j)
                else:
                    a=rook(a,i,j)
    return len([i for i in sum(a,[]) if not i])
                    


print(bishops_and_rooks([
 [1,0,0,0,0,0,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,-1,0,0,1,0,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,0,0,-1,-1,0,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,0,0,0,0,0,0,0]]))
print(bishops_and_rooks([
 [0,0,0,0,0,1,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,-1,1,0,1,0,0,0], 
 [0,0,0,0,0,-1,0,0], 
 [0,0,0,0,0,0,0,0], 
 [0,0,0,1,0,0,0,0], 
 [-1,0,0,0,0,0,0,0]]))

[['&', '&', '&', '&', '&', 1, '&', '&'],
 [0, 0, '&', '&', '&', '&', 0, 0],
 [0, 0, '&', '&', '&', '&', 0, '&'],
 [0, -1, 1, '&', 1, '&', '&', '&'],
 ['&', 0, '&', '&', '&', -1, 0, 0],
 [0, 0, '&', '&', '&', 0, '&', 0],
 ['&', '&', '&', 1, '&', '&', '&', '&'],
 [-1, 0, '&', '&', '&', '&', 0, 0]]