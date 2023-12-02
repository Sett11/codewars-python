def hungry_foxes(s):
    if 'F' not in s or 'C' not in s:
        return s
    if '[' not in s and 'F' in s:
        return s.replace('C','.')
    
    g=[list(i) for i in zip([i for i,j in enumerate(s) if j=='['],[i for i,j in enumerate(s) if j==']'])]
    r=[[0,g[0][0]]]

    for i in range(len(g)-1):
        r.append([g[i][1],g[i+1][0]])
    
    r.append([g[-1][1],len(s)])
    s=list(s)

    for i,j in g:
        if 'F' in s[i+1:j]:
            s[i+1:j]=['.' if j=='C' else j for j in s[i+1:j]]
    
    if any('F' in s[i:j] for i,j in r):

        for i,j in r:
            s[i:j]=['.' if j=='C' else j for j in s[i:j]]

    return ''.join(s)

print(hungry_foxes("C.C[]C.[CC..FCCC.CC.CC..CC.CCC.C.CC.CC]...FC"))