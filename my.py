def f(i,a,s):
    j=i
    while j<len(a):
        t=s[0]-a[j]
        if not (t&1):
            s.pop(0)
            s=[a[j]]+s
            s.append(t)
            return f(j+1,a,s)
        else:
            j+=1
    return s

def peel_the_onion(s,d):
    a,b=[i**d for i in range(1,s+1)][::-1],[s**d]
    return a if len(a)==1 else a[::-1][-1:] if len(a)==2 else sorted(f(1,a,b),reverse=True)

print(peel_the_onion(5,3))