def lyrics_print(a):
    r=[]
    def f(x):
        t=[]
        a=[i for i in x.copy()]
        for i in reversed(range(len(a))):
            for j in reversed(range(len(a[i]))):
                t.append([k for k in a.copy() if k])
                a[i]=a[i][:j]
        return t[::-1]
    for i in a:
        x=f(i)
        for j in range(len(x)):
            x[j][-1]=x[j][-1]+'_'
        r.extend(x)
    return r

print(*lyrics_print([
         ['Hey','you',],
         ['Good','luck',],
     ]),sep='\n')