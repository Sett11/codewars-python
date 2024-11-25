def dots_and_boxes(a):
	d,c,r,u,q=[0]*2,0,[i for i in range(0,max(sum([list(i) for i in a],[]))+1)],set(),set()
	l=len(r)
	k=int(l**.5)
	r=[r[i:i+k] for i in range(0,l,k)]
	def f():
		w=set()
		for i in range(k-1):
			for j in range(k-1):
				t=((r[i][j],r[i][j+1]),(r[i][j+1],r[i+1][j+1]),(r[i+1][j],r[i+1][j+1]),(r[i][j],r[i+1][j]))
				if t not in q and all(x in u for x in t):
					w.add(t)
		return w
	for i in a:
		u.add(tuple(sorted(i)))
		x=f()
		if x:
			q.update(x)
			d[c]+=len(x)
		else:
			c=1 if c==0 else 0
	return tuple(d)
		

print(dots_and_boxes(((0,1),(7,8),(1,2),(6,7),(0,3),(5,8),(3,4),(1,4),(4,5),(2,5),(4,7),(3,6))))
print(dots_and_boxes(((0,1),(1,2),(2,5),(5,4),(4,7),(7,8),(8,5),(1,4),(6,7),(3,6),(3,0),(3,4))))