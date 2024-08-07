def build_trie(*args):
    t={}
    def insert(s):
        c,x,n=t,'',len(s)
        for i in range(n):
            x+=s[i]
            if x in c and c[x] is None and i!=n-1:
                c[x]={}
            if x not in c:
                c[x]={} if i!=n-1 else None
            c=c[x]
    for i in args:
       insert(i)
    return t
   
print(build_trie("A","to", "tea", "ted", "ten", "i","in","inn"))