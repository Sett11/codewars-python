def f(a,i,j):
    if i==len(a):
        a.append([0]*len(a[0]))
        return a,i,j
    elif i==-1:
        a.insert(0,[0]*len(a[0]))
        return a,0,j
    elif j==len(a[0]):
        a=[k+[0] for k in a]
        return a,i,j
    elif j==-1:
        a=[[0]+k for k in a]
        return a,i,0
    return a,i,j

def q(i,j,d,v):
    if not v:
        if d==0:
            return i,j-1,3
        if d==1:
            return i-1,j,0
        if d==2:
            return i,j+1,1
        if d==3:
            return i+1,j,2
    else:
        if d==0:
            return i,j+1,1
        if d==1:
            return i+1,j,2
        if d==2:
            return i,j-1,3
        if d==3:
            return i-1,j,0

def ant(a,j,i,n,d=0):
    while n:
        v=a[i][j]==1
        a[i][j]=int(not bool(a[i][j]))
        i,j,d=q(i,j,d,v)
        a,i,j=f(a,i,j)
        n-=1
    return a

print(ant([
            [1,0,1],
            [0,1,0],
            [1,0,1],
        ],1,1,5,0))

print(ant([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2, 137, 1))