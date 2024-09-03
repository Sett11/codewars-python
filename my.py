# def palin(a,b):
#     n=int(str(1)+('0'*(a-1)))
#     while b:
#         s=str(n)
#         if s==s[::-1]:
#             b-=1
#         n+=1
#     return n-1

# print(palin(6,20))

from itertools import permutations as perm

def f(a,j,r,q):
   if not r:
      t=[]
      for i in range(j):
         t.append(a[i])
      q.append(t)
      return
   p=1 if j==0 else a[j-1]
   for i in range(p,r+1):
      a[j]=i
      f(a,j+1,r-i,q)
   return q

def indices(n,d):
   return sum([[list(k) for k in set(j for j in perm([0]*(n-len(i))+i)) if len(k)==n] for i in f([0]*d,0,d,[])],[]) if d else [[0]*n]

print(indices(3,4))