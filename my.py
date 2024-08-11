def bounding_box(arr):
    z=[i for i in zip(*sum([[[k,i] for i,j in enumerate(p) if j==1] for k,p in enumerate(arr)],[]))]
    if not z:
        return arr
    r=[[0]*len(arr[0]) for _ in range(len(arr))]
    a,b,x,y=min(z[0]),min(z[1]),max(z[0]),max(z[1])
    r[a][b:y+1]=r[x][b:y+1]=[1]*(y-b+1)
    for i in range(a,x+1):
        r[i][b]=r[i][y]=1
    return r

print(*bounding_box([[0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,1,1,0,0,0,0],
 [0,0,0,1,1,1,1,0,0,0],
 [0,0,1,1,1,1,1,1,0,0],
 [0,1,1,1,1,1,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0]]),sep='\n')