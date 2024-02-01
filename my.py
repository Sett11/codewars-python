def f(a=[[1],[1,1],[1,2,1]],k=250):
    if not k:
        return a
    t=[1]
    for i in range(1,len(a[-1])):
        t.append(a[-1][i-1]+a[-1][i])
    a.append(t+[1])
    return f(a,k-1)
r=f()

def easyline(n):
    return sum(map(lambda x:x**2,r[n]))

print(easyline(13))