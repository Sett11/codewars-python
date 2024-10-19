def zfunc(s):
	n=len(s)
	z=[n]+[0]*(n-1)
	l=r=0
	for i in range(1,n):
		if i>r:
			l=r=i
			while r<n and s[r-l]==s[r]:
				r+=1
			z[i]=r-l
			r-=1
		else:
			k=i-l
			if z[k]<r-i+1:
				z[i]=z[k]
			else:
				l=i
				while r<n and s[r-l]==s[r]:
					r+=1
				z[i]=r-l
				r-=1
	return z if n else []
	

print(zfunc('ababcaba'))