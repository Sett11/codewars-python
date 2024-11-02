def converge(g,a,b,c):
    if a==b==c:
        return 0
    q=tuple([tuple([a]),tuple([b]),tuple([c])])
    w=set(q)
    for i in range(len(g)):
        q=[set(k for j in i for k in g[j]) for i in q]
        if q[0]&q[1]&q[2]:
            return i+1
        q=tuple(map(tuple,q))
        if q in w:
            return
        w.add(q)
    return i
        

print(converge({
            0: {5, 1, 3},
            1: {0, 2},
            2: {1},
            3: {0, 4},
            4: {3},
            5: {6, 0},
            6: {5},
        },2,4,6))

print(converge({
            1: {2, 3},
            2: {1, 3},
            3: {1, 2},
        },1,2,3))