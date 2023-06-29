def f(x):
    while x[0]==0:
        x=x[1:]
    while x[-1]==0:
        x=x[:-1]
    return x.count(1)==len(x)

def replace_zero(a):
    print(a)
    if f(a) and a[-1]==0:
        return len(a)-a[::-1].index(1)
    if f(a) and a[-1]!=0:
        return a.index(1)-1
    if a.count(1)==3 and a[-1]==1 and a[-2]==1 and a[-3]!=1:
        return len(a)-3
    if a.count(1)==3 and a[0]==1 and a[1]==1 and a[2]!=1:
        return 2
    if a.count(1)==3 and a[0]!=1 and a[1]==1 and a[2]==1 and a[3]!=1:
        return 3
    if a.count(1)==4 and a[-1]==1 and a[-2]==1 and a[-3]==1 and a[-4]!=1:
        return len(a)-4
    if a.count(1)==4 and a[-1]==1 and a[-2]==1 and a[-3]!=1:
        return len(a)-3
    if a.count(1)==1 and a[-1]!=1:
        return a.index(1)+1
    if a.count(1)==1 and a[-1]==1:
        return a.index(1)-1
    if a.count(1)==2 and a[-1]==1 and a[-1]==1 and a[-2]!=1:
        return len(a)-2
    if a.count(1)==2 and a[-1]==1 and  a[-2]!=1:
        return len(a)-2
    if a.count(1)==2 and a[-1]!=1 and  a[-2]==1 and a[-3]!=1 and a[-4]!=1:
        return len(a)-1
    n=0
    a.append(0)
    if a[0]!=1:
        a.insert(0,1)
        n=1
    i,l,j,v,m=0,[],-1,-1,0
    while i<len(a):
        if j!=-1 and v!=-1 and not a[i] and v!=j:
            t=len(a[j:i])
            m=max(m,t)
            l.append([t,v])
            i=v+1
            j=-1
            v=-1
        if a[i]==1 and j==-1:
            j=i
        if j!=-1 and not a[i]:
            v=i
        i+=1
    return [i for i in l if i[0]==m][::-1][0][1]-n


print(replace_zero([0, 1, 1, 1, 0, 0]))
print(replace_zero([1, 0, 0, 0, 1, 1]))