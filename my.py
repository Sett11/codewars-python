from math import ceil
from copy import deepcopy

def encode(s):
	n=ceil(len(s)**.5)
	a,q,w=[[1]*n for _ in range(n)],[(0,0),(0,n-1),(n-1,n-1),(n-1,0)],list(s[::-1])
	r=deepcopy(q)
	while w:
		for x,y in r:
			if not w:
				break
			if a[x][y]!=1:
				q[0],q[1],q[2],q[3]=(q[0][0]+1,q[0][1]+1),(q[1][0]+1,q[1][1]-1),(q[2][0]-1,q[2][1]-1),(q[3][0]-1,q[3][1]+1)
				r=deepcopy(q)
				break
			a[x][y]=w.pop()
		else:
			r[0],r[1],r[2],r[3]=(r[0][0],r[0][1]+1),(r[1][0]+1,r[1][1]),(r[2][0],r[2][1]-1),(r[3][0]-1,r[3][1])
	return ''.join(''.join([j if j!=1 else ' ' for j in i]) for i in a)

def decode(s):
	l=len(s)
	n=ceil(l**.5)
	a,q,c=[list(s[i:i+n]) for i in range(0,l,n)],[(0,0),(0,n-1),(n-1,n-1),(n-1,0)],''
	r=deepcopy(q)
	while len(c)<l:
		for x,y in r:
			if a[x][y]==1:
				q[0],q[1],q[2],q[3]=(q[0][0]+1,q[0][1]+1),(q[1][0]+1,q[1][1]-1),(q[2][0]-1,q[2][1]-1),(q[3][0]-1,q[3][1]+1)
				r=deepcopy(q)
				break
			c+=a[x][y]
			a[x][y]=1
		else:
			r[0],r[1],r[2],r[3]=(r[0][0],r[0][1]+1),(r[1][0]+1,r[1][1]),(r[2][0],r[2][1]-1),(r[3][0]-1,r[3][1])
	return c.strip()
		
	
# print(encode('I would be presumptuous, indeed, to present myself against the distinguished gentlemen to whom you have listened if this were but a measuring of ability; but this is not a contest among persons. The humblest citizen in all the land when clad in the armor of a righteous cause is stronger than all the whole hosts of error that they can bring.'))
# print(decode('Iubrmo e pemlgshin is teoooale t etmhlisug l;tistceagrrged nshueczilhaw . letuead  ofrtsui eanpnrnnstgt   lortmi uas   s erahcoeas mie tlah bg  rrhri ue d tuo     . a esvtstoahet     ttin ir  i  lh     ewel nn,hhionon   iae eoiydyu m  ny trfssnshf,hylent hhlaroshmwautihn ecoga rhic  tumfTled   nttb  s epnnopotnan tbtboies daabeifese  w eeegout  i steodnsts dw'),sep='\n')
print(decode('Stsgiriuar i ninmd l otac'),sep='\n')
print(decode('Rntodomiimuea  m'),sep='\n')