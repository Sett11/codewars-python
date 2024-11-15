def unpack(l):
    r=[]
    def f(x):
        if isinstance(x,(str,int)) or not x:
            r.append(x)
            return
        if isinstance(x,dict):
            for i in x:
                f(i)
                f(x[i])
        elif isinstance(x,(list,tuple,set)):
            for i in x:
                f(i)
    for i in l:
        f(i)
    return r

print(unpack(['x', [1, 2, 4, [(1, 2), 3, 'y', 13], [1]], 1, 2, 12, {1, 2, 3}, {(1, 2): 'b', 'c': (3, 4)}]))