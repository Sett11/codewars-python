class Item:
      def __init__(self,weight=0,price=0):
            self.weight=weight
            self.price=price

def get_w_p(a):
    a=sorted(a,key=lambda x:(x.price),reverse=True)
    d={}
    for i in range(len(a)):
          d[i]=(a[i].weight,a[i].price)
    return [d[item][0] for item in d],[d[item][1] for item in d]   

def get_mat(d,A):
      w,p=get_w_p(d)
      n=len(p)
      V=[[0 for _ in range(A+1)] for __ in range(n+1)]
      for i in range(n+1):
            for a in range(A+1):
                  if i==0 or a==0:
                        V[i][a]=0
                  elif w[i-1]<=a:
                        V[i][a]=max(p[i-1] + V[i-1][a-w[i-1]], V[i-1][a])
                  else:
                        V[i][a]=V[i-1][a]       
      return V,w,p

def greedy_thief(d,A):
      V,w,p=get_mat(d,A)
      n=len(p)
      res,a,r=V[n][A],A,[]
      for i in range(n,0,-1):
            if res<=0:
                  break
            if res==V[i-1][a]:
                  continue
            else:
                  r.append((w[i-1],p[i-1]))
                  res-=p[i-1]
                  a-=w[i-1]
      return [Item(*i) for i in r]

print(greedy_thief([Item(weight=0, price=16), Item(weight=7, price=13), Item(weight=20, price=2), Item(weight=27, price=42), Item(weight=7, price=21), Item(weight=17, price=30), Item(weight=0, price=8), Item(weight=0, price=22), Item(weight=12, price=20), Item(weight=3, price=18), Item(weight=2, price=28), Item(weight=18, price=1), Item(weight=15, price=30), Item(weight=17, price=23), Item(weight=15, price=16), Item(weight=27, price=21), Item(weight=7, price=10), Item(weight=25, price=30), Item(weight=17, price=30), Item(weight=29, price=7), Item(weight=23, price=24), Item(weight=1, price=47), Item(weight=21, price=48), Item(weight=18, price=32), Item(weight=13, price=32), Item(weight=29, price=48), Item(weight=0, price=37), Item(weight=6, price=37), Item(weight=0, price=24), Item(weight=28, price=15), Item(weight=19, price=25), Item(weight=6, price=43), Item(weight=26, price=11), Item(weight=16, price=16), Item(weight=6, price=3), Item(weight=9, price=23), Item(weight=13, price=48), Item(weight=0, price=11), Item(weight=7, price=41), Item(weight=0, price=39)],286))