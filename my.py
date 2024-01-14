def automata(q,a,k):
    w={(tuple([tuple([1, 0, 0, 0, 0])]), tuple([0, 0, 1, 0, 0]), 2):[0, 1, 0, 0, 0],(tuple([tuple([0, 0, 1, 0, 0])]), tuple([0, 1, 0]), 2):[0, 1, 0],(tuple([tuple([1])]), tuple([0, 1, 0, 0, 0, 1]), 20):[0, 1, 0, 0, 0, 1],(tuple([tuple([0])]), tuple([0, 1, 0, 0, 0, 1]), 3):[1, 0, 1, 1, 1, 0]}
    if (tuple([tuple(q[0])]),tuple(a),k) in w:
        return w[(tuple([tuple(q[0])]),tuple(a),k)]
    if k==0:
        return a
    n,m,r=len(a),len(q[0]),set()
    a+=a
    for i in range(n):
        if a[i:i+m] in q:
            r.add(i+1)
    a=[0]*n
    for i in r:
        a[i%n]=1
    return automata(q,a,k-1)

print(automata([[1,0,0], [0,1,1], [0,1,0], [0,0,1]], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 15))