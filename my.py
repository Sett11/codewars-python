def d(a):
    m,n,z=len(a),len(a[0]),[]
    for r in range(m):
        i,j,v=r,0,[]
        while j<n and i>=0:
            v.append(a[i][j])
            j+=1
            i-=1
        z.append(v[::-1])
    for c in range(1,n):
        i,j,v=m-1,c,[]
        while j<n and i>=0:
            v.append(a[i][j])
            j+=1
            i-=1
        z.append(v[::-1])
    return z

is_wristband=lambda a:all([all([j==i[0] for j in i]) for i in a]) or all([all([j==i[0] for j in i]) for i in zip(*a)]) or all([all([j==i[0] for j in i]) for i in d(a)]) or all([all([j==i[0] for j in i]) for i in d(a[::-1])])

print(is_wristband([['A', 'A'], 
        ['B', 'B'], 
        ['C', 'C']]))
print(is_wristband([['A', 'B'], 
        ['A', 'B'], 
        ['A', 'B']]))
print(is_wristband([
    ['A', 'B', 'C'], 
    ['C', 'A', 'B'], 
    ['D', 'C', 'A'], 
    ['E', 'D', 'C']]))
print(is_wristband([['A', 'B', 'C'], 
        ['B', 'C', 'A'], 
        ['C', 'A', 'B'], 
        ['A', 'B', 'A']]))