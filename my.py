# from bisect import bisect_right as br

# happy,no_happy=set(),set()

# def f(x):
#     if x in happy or x in no_happy:
#             return
#     u,t=set([x]),[x]
#     while 1:
#         x=sum([int(i)**2 for i in list(str(x))])
#         t.append(x)
#         if x==1:
#             happy.update(t)
#             return
#         if x in u:
#             no_happy.update(t)
#             return
#         u.add(x)

# {f(i) for i in range(2,1000000)}
# res=sorted(happy)

# def perf_happy(n):
#     return res[:br(res,n)]

# print(perf_happy(999))

def doors(n):
    return len([i*i for i in range(1,int(n**.5+1))])