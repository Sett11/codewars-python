def f(n):
    r=set([1,n])
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            r.update([i,n//i])
    return sum(r)

def find_int(a,b,c):
    r=[]
    for i in range(a,b+1):
        t=list(map(int,str(i)))
        h=t.copy()
        for j in range(len(t)):
            t[j]*=(j+1)
            h[j]=(j+1)**h[j]
        t,h=sum(t),sum(h)*c
        if h%f(t)==0:
            r.append(i)
    return len(r),r

print(find_int(100,200,1))