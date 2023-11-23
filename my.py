def apple_boxes(k):
    y=r=0

    for i in range(1,k+1):
        if i&1:
            y+=i*i
        else:
            r+=i*i
    
    return r-y
    

print(apple_boxes(36))

def make_spanning_tree(a,m):
    a=sorted(a,key=lambda e:e[1])
    s=sorted(set(''.join([i[0] for i in a])))
    g={i:set() for i in s}
    
    for i in g:
        for j,k in a:
            if i in j:
                p=[h for h in j if h!=i][0]
                g[i].add((p,k))

    for i in g:
        g[i]=dict(g[i])
    
    return g


print(make_spanning_tree([
            ('AB', 1), ('AE', 1), ('BA', 1), ('EA', 1), ('GH', 1), ('HG', 1), ('AF', 2), ('DE', 2),
            ('DH', 2), ('ED', 2), ('FG', 2), ('FA', 2), ('GF', 2), ('HD', 2), ('BE', 3), ('CD', 3),
            ('DC', 3), ('EB', 3), ('DG', 4), ('EF', 4), ('FE', 4), ('GD', 4), ('AH', 5), ('BF', 5),
            ('FB', 5), ('HA', 5), ('BC', 6), ('CB', 6), ('CH', 7), ('HC', 7), ('CG', 8), ('GC', 8)
        ],'min'))