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

def type_out(s):
    s=s.replace('[shift][unshift]','').replace('[holdshift][unshift]','')
    def f(x,v):
        if v:
            x=x.capitalize()
        for i in range(len(x)):
            p,t=x[:i],x[i:]
            if t.startswith('[holdshift]'):
                k=t.index('[unshift]')
                x=p+x[i:i+9+k].replace('[holdshift]','').replace('[unshift]','').upper()+x[i+9+k:]
        return x
    a,v=s.split('[shift]'),s.startswith('[shift]')
    if len(a)==1:
        return f(a[0],v)
    return f(a[0],v)+''.join(f(i,True) for i in a[1:])

print(type_out('vvv[holdshift]uppercase[unshift] lowercase and [holdshift]uppercase[unshift] again'))
print(type_out('[shift][unshift]dont shi[shift][unshift]ft th[shift][unshift]is'))
print(type_out('[holdshift]holdshift[unshift] [shift]shift'))