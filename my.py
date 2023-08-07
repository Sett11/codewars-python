def f(a):
    i=0
    while i<len(a):
        j=0
        if a[i][0]=='_':
           while j<len(a[i]):
               if a[i][j].isalpha():
                a[i][0]=a[i][j]
                a[i][j]='_'
                break
               j+=1
        i+=1
    return a

def alphabet_war(r,a):
    q,w,n=[],[[j if j.isalpha() else 'x' for j in list(i)] for i in zip(*r)],0
    for i in a:
        t=[]
        for k,j in enumerate(i):
            if j=='*':
                t.append([k-1,k,k+1])
        if t:
            q.append(list(set([h for h in sum(t,[]) if h>=0 and h<len(r[0])])))
    while n<len(q):
        j=0
        while j<len(q[n]):
            w[q[n][j]][0]='_'
            j+=1
        w=f(w)
        n+=1
    return [''.join(i) for i in zip(*w)][0]

print(alphabet_war(["abcdefg","hijklmn"],["   *   ", "*  *   "]))
print(alphabet_war(["aaaaa","bbbbb", "ccccc", "ddddd"],  ["*", " *", "   "]))
print(alphabet_war(["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ],["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]))