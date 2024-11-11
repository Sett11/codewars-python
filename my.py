from copy import deepcopy

def black_hole(n,i,j):
	a,q,w=[[' ']*n for _ in range(n)],[(0,0),(0,n-1),(n-1,n-1),(n-1,0)],list(range(n**2,0,-1))
	r=deepcopy(q)
	while w:
		for x,y in r:
			if not w:
				break
			if a[x][y]!=' ':
				q[0],q[1],q[2],q[3]=(q[0][0]+1,q[0][1]+1),(q[1][0]+1,q[1][1]-1),(q[2][0]-1,q[2][1]-1),(q[3][0]-1,q[3][1]+1)
				r=deepcopy(q)
				break
			a[x][y]=w.pop()
		else:
			r[0],r[1],r[2],r[3]=(r[0][0],r[0][1]+1),(r[1][0]+1,r[1][1]),(r[2][0],r[2][1]-1),(r[3][0]-1,r[3][1])
	return a[i][j]
		
print(black_hole(5,3,2),sep='\n')