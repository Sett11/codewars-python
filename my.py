def start(a):
    n,m=len(a),len(a[0])
    r=[[0]*m for _ in range(25)]
    q=[0]*35
    a=r+a+r
    n=len(a)

    for i in range(n):
        a[i]=q+a[i]+q

    return a

def end(a):
    n=len(a)
    i=0
    j=n-1

    while i<n:
        if a[i].count(1):
            break
        i+=1
    
    while j:
        if a[j].count(1):
            break
        j-=1
    
    a=a[i:j+1]
    q=[list(i) for i in zip(*a)]
    k=0
    h=len(q)-1

    while k<len(q):
        if q[k].count(1):
            break
        k+=1

    while h:
        if q[h].count(1):
            break
        h-=1
    
    for i in range(len(a)):
        a[i]=a[i][k:h+1]
    
    return a

def generate(a,w):
    n,m=len(a),len(a[0])
    r=[]

    for i in range(n):
        for j in range(m):
            t=[a[p][k] for p,k in [[i+1,j],[i,j+1],[i-1,j],[i,j-1],[i-1,j-1],[i+1,j+1],[i-1,j+1],[i+1,j-1]] if p>=0 and p<n and k>=0 and k<m]
            c=t.count(1)
            if a[i][j]:
                if c<2 or c>3:
                    r.append([[i,j],0])
            else:
                if c==3:
                    r.append([[i,j],1])
    
    for i,j in r:
        if j:
            a[i[0]][i[1]]=1
        else:
            a[i[0]][i[1]]=0
    
    return a if w<=1 else generate(a,w-1)

def get_generation(a,n):
    return end(generate(start(a),n)) if n else a



print(get_generation([
            [1,0,0],
            [0,1,1],
            [1,1,0]
        ], 1))

print(get_generation([[1, 1, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1]],16))