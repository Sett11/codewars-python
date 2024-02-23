def f(n):
    k,c,a=3,1,[]
    while k<n:
        c+=1
        k=3**c
        a.append(k)
    if a and a[-1]==n:
        return k,c
    return a[-2] if len(a)>1 else a[-1] if a else 3,c-1 if c!=1 else 1

def sum_of_threes(n):
    q=n
    if n==1:
        return '3^0'
    if n<3:
        return 'Impossible'
    r=[]
    while n>=3:
        a,b=f(n)
        r.append(b)
        n-=a
    if len(set(r))!=len(r):
        return 'Impossible'
    w=0
    s=''
    for i in r:
        s+=f'3^{i}+'
        w+=3**i
    return s[:-1]+('+3^0' if w!=q else '')

print(sum_of_threes(1418194818))