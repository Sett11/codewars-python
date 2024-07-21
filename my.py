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

u,time=set(),[]

for i in range(24):
    i%=24
    for j in range(60):
        j%=60
        for k in range(60):
            k%=60
            v=len(set([k-j,j-i]))==1
            z,w,q=k-j in [0,1,2],i<j<k,len(set([i%10,j%10,k%10]))==1
            r=f"{('0' if i<10 else '')+str(i)}:{('0' if j<10 else '')+str(j)}:{('0' if k<10 else '')+str(k)}"
            t=''.join(r.split(':'))
            if (v and w and z) or (q and v) or (v and k-j==i) or (t==t[::-1] and len(set(t))==2) or r=='12:34:56':
                time.append(r)
                u.add(r)

time=sorted([i if i!='00:00:00' else '24:00:00' for i in time])

def next_good_time(s):
    return next('00'+i[2:] if i.startswith('24') else i for i in time if i>s)

print(next_good_time('00:00:00'))
print(next_good_time('23:52:18'))
print(next_good_time('14:04:49'))
print(next_good_time('13:58:25'))