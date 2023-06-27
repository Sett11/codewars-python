def verify_latin_square(a,m):
    if len([i for i in a if len(i)!=len(a)]):
        return 'Array not square'
    if len([i for i in a if len(i)!=m]) or len(a)!=m:
        return 'Array is wrong size'
    t=[[i,j] for j,i in enumerate(a) if len(i)!=len(set(i))]
    if len(t):
        return f'{[i for i in t[0][0] if t[0][0].count(i)>1][0]} occurs more than once in row {t[0][1]+1}'
    t=[[i,j] for j,i in enumerate([list(i) for i in zip(*a)]) if len(i)!=len(set(i))]
    if len(t):
        return f'{[i for i in t[0][0] if t[0][0].count(i)>1][0]} occurs more than once in column {t[0][1]+1}'
    t=[]
    [t.extend(i) for i in a]
    t=[i for i in t if i>m or i<1]
    if len(t):
        v=[x[0] for x in [[[i,k] for i,j in enumerate(n) if j==t[0]] for k,n in enumerate(a)] if len(x)]
        return f'{t[0]} at {v[0][1]+1},{v[0][0]+1} is not between 1 and {m}'
    return f'Valid latin square of size {m}'

print(verify_latin_square([[1, 3, 2], [3, 2, 1], [3, 1, 2]],3))