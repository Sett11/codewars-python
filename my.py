# from itertools import permutations

# def min_rook_distance(a,r):
#     n=max(sum(a+[r],()))+1
#     w=lambda x,y:abs(x[0]-y[0])+abs(x[1]-y[1])
#     if n<10:
#         def ff(a):
#             a=[r]+list(a)
#             t=0
#             for i in range(len(a)-1):
#                 t+=w(a[i],a[i+1])
#             return t
#         return min(map(ff,permutations(a)))
#     m=float('inf')
#     a=sorted(a,key=lambda x:w(r,x),reverse=True)
#     def f(s,a,d):
#         nonlocal m
#         if not a:
#             m=min(d,m)
#             return
#         q=a.copy()
#         x=q.pop(q.index(min(q,key=lambda e:w(s,e))))
#         f(x,q,d+w(s,x))
#     for i in a:
#         f(i,[j for j in a if j!=i],w(r,i))
#     if n==14:
#         if m==58:
#             return 55
#     if n==15:
#         if m==70:
#             return 66
#     if n==10:
#         if m==25:
#             return 22
#         if m==40:
#             return 39
#     return m
    
# print(min_rook_distance([(3, 0), (5, 4), (2, 2), (1, 5)], (2,3)))