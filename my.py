from re import sub

WORDS=list(map(lambda x:x.lower(),WORDS))

def transform(s,j):
    al='abcdefghijklmnopqrstuvwxyz'
    return ''.join([al[(al.index(i)+j)%len(al)] for i in s])

def break_caesar(s):
    a=[sub(r'[^A-z]','',i).lower() for i in s.split()]
    i=m=0
    d={}
    while i<26:
        n=sum(j in WORDS for j in [transform(k,i) for k in a])
        m=max(n,m)
        d[n]=i
        i+=1
    return 26-d[m] if d[m] else 0