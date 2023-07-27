def f(a):
    l,c,r,i,k,p=len(a),[0 for i in a],[''.join(a)],1,0,0
    while i<l:
        if c[i]<i:
            k,p=i%2 and c[i],a[i]
            a[i]=a[k]
            a[k]=p
            c[i]+=1
            i,s=1,''.join(a.copy())
            if s not in r:
                r.append(s)
        else:
            c[i]=0
            i+=1
    return r

def get_words(h):
    a=[]
    [a.append(''.join(i*h[i])) for i in h]
    return sorted(f(list(''.join(a))))

print(get_words({2:["a"], 1:["b", "c"]}))