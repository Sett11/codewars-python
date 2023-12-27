# def f(a,j,n,r,q=[]):
#     if(r<0):
#         return
#     if(r==0):
#         t=[]
#         for i in range(j):
#             t.append(a[i])
#         q.append(t)
#         return
#     p=1 if j==0 else a[j-1]
#     for k in range(p,n+1):
#         a[j]=k
#         f(a,j+1,n,r-k,q)
#     return q

# def combos(n):
#     return f([0]*n,0,n,n,[])

# print(combos(30))

from math import prod

def find_part_max_prod(n):
    a,b=divmod(n,3)
    if not b:
        r=[3]*a
        return [r,prod(r)]
    if b==2:
        r=[3]*a+[2]
        return [r,prod(r)]
    r1,r2=[4]+[3]*(a-1),[3]*(a-1)+[2,2]
    return [r1,r2,prod(r1)]


print(find_part_max_prod(8))
print(find_part_max_prod(10))
print(find_part_max_prod(40))
print(find_part_max_prod(43))