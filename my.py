def crossedwords(a,b):
    r,k=[],next(i for i,j in enumerate(b) if j in a)
    q=a.index(b[k])
    for i in range(len(b)):
        if i!=k:
            t=''.join(' ' if j!=q else b[i] for j in range(len(a)))
            r.append(t)
        else:
            r.append(a)
    return '\n'.join(r)+'\n'

print(crossedwords('ABXC', 'WXYZ'))
print(crossedwords('GRAPHICAL', 'SYNTHESIS'))