def f(n,l):
    a,r,c,t,x=[i for i in range(1,n*n*4+1)],[],n,[],[]
    while len(a):
        x.append(a.pop(0))
        if(len(x)==c):
            r.append(x)
            x=[]
            c=c-1 if c==n+1 else c+1
    while len(r)>n*2+1:
        r=r[:-1]
    for i in range(0,len(r)-1,2):
        for j in range(len(r[i])):
            t.append([r[i][j],r[i+1][j],r[i+1][j+1],r[i+2][j]])
    m=[k[1][0] for k in [[i,[j for j in i if j not in l]] for i in t] if len(k[1])==1]
    return sorted(list(set(l))) if not len(m) else f(n,m+l)

class Game():
    def __init__(self,n):
        self.n=n
    def play(self,l):
        return f(self.n,l)
    
r=Game(1)

print(r.play([1,2,3,4]))