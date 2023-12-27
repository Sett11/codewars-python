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


def pow_root_pandigit(v,n,k):
    f,m,r,c=lambda x:len(set(str(x)))==len(str(x)) and '0' not in str(x),int(pow(v,1/n))+1,[],0
    while len(r)<k and c<min(m*2,15000):
        t=m**n
        if f(m) and f(t) and t>v:
            r.append([m,t])
        c+=1
        m+=1
    return r if len(r)>1 or not r else r[0]
    

print(pow_root_pandigit(388,2,3))
print(pow_root_pandigit(1728,3,4))
print(pow_root_pandigit(5022,2,7))