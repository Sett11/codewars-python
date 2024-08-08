from itertools import groupby

def radix_tree(*s):
    t={}
    def f(a,tr):
        r=[list(j) for _,j in groupby(sorted(a),key=lambda x:x[0] if x else '')]
        if all(len(i)==1 for i in r):
            for i in r:
                if i[0]:
                    tr[i[0]]={}
            return
        for i in r:
            g=next(iter(k for k,p in enumerate([set(j) for j in zip(*i)]) if len(p)>1),min([len(x) for x in i]))
            pr=i[0][:g]
            if pr:
                tr[pr]={}
            for j in range(len(i)):
                i[j]=i[j][g:]
            if all(not x for x in i):
                continue
            f(i,tr[pr])
    f(s,t)
    return t

print(radix_tree("romane", "romanus", "romulus", "rubens", "rubicon", "rubicundus"))
print(radix_tree('test', 'tester', 'testers'))