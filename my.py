def find_ways(initial_num,target_num,*,must_include=None,must_avoid=None):
    def check(a):
        n=initial_num
        w=[]
        for i in a:
            if i==1:
                n+=3
            if i==2:
                n+=sum(map(int,str(n).replace('-','')))
            if i==3:
                n+=n%4
            w.append(n)
        if must_include:
            if not all(i in w for i in must_include):
                return False
        return n==target_num
    r=set()
    def f(n,q,w):
        if (must_avoid and n in must_avoid) or n>target_num:
            return
        if n==target_num:
            if check(q):
                r.add(tuple(q))
            return
        w.add(n)
        f(n+3,q+[1],w)
        f(n+sum(map(int,str(n).replace('-',''))),q+[2],w) if n else None
        f(n+n%4,q+[3],w) if n%4 else None
    f(initial_num,[],set())
    return len(r)

print(find_ways(1,27,must_include = [16], must_avoid = [25, 5, 7]))