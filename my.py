def L(a,b,c,d) :
    g=[b or 0,c or 0]
    while len(g)<a:
        g.append(g[len(g)-1]+g[len(g)-2]+d)
    return g

print(L(10, 0, 1, 4))