# def comb(n,r):
#     res=[]
#     t=[0]*r
#     def f():
#         q=[i for i in t]
#         if len(q)==len(set(q)):
#             res.append(q)
#     while 1:
#         for i in reversed(range(r)):
#             if t[i]!=i+n-r:
#                 break
#         else:
#             return res
#         t[i]+=1
#         for j in range(i+1,r):
#             t[j]=t[j-1]+1
#         f()

# def pair_em_up(n):
#     return sorted(sum([comb(n,i) for i in range(2,n+(1 if n%2==0 else 0),2)],[]),key=lambda x:(x[0],-len(x)))

# print(pair_em_up(20))

from math import ceil

def get_missing_ingredients(r,a):
    n=max([ceil(a[i]/r[i]) for i in a if i in r],default=0)
    if not n:
        return r
    d={i:r[i]*n-a[i] for i in a if i in r}
    for i in r:
        if i not in d:
            d[i]=r[i]*n
    return {i:d[i] for i in d if d[i]}

print(get_missing_ingredients({"flour": 200, "eggs": 1, "sugar": 100}, {"flour": 123, "eggs": 70}))
print(get_missing_ingredients({"flour": 200, "eggs": 1, "sugar": 100}, {"flour": 100}))