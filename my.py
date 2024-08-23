sq={i*i:i for i in range(2,50)}

def ham(g,i,n,p):
   if i not in p:
      p.append(i)
      if len(p)==n:
         return p
      for j in g.get(i,[]):
         r=[i for i in p]
         t=ham(g,j,n,r)
         if t:
            return t

def square_sums_row(n):
   g={}
   for i in range(1,n+1):
      for j in range(1,n+1):
         if i!=j and i+j in sq:
            if i not in g:
               g[i]=[j]
            else:
               g[i].append(j)
   for i in range(1,n+1):
      t=ham(g,i,n,[])
      if t:
         return t
   return False
                

print(square_sums_row(43))