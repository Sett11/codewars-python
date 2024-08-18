def compound_match(a,s):
    u,r,q=set(a),[],[]
    for i in range(len(s)):
        t,p=s[:i],s[i:]
        if t in u and p in u:
            r.extend([t,p])
            break
    for i in range(len(a)):
        if a[i] in (t,p) and a[i] not in [j[0] for j in q]:
            q.append((a[i],i))
        if len(q)==2:
            q=dict(sorted(q,key=lambda x:r.index(x[0])))
            return sorted(r,key=lambda x:q[x])+[list(q.values())]

print(compound_match(['bow','crystal','organic','ally','rain','line'],'crystalline'))
print(compound_match(['ally', 'spell', 'less', 'knight', 'land', 'tale', 'tar', 'guile', 'folk', 'shear', 'land', 'tar', 'fall', 'bow', 'bed', 'grab', 'guile', 'red', 'super', 'top', 'line', 'bowl', 'red', 'wind', 'deck', 'let', 'in', 'tree', 'ally', 'ally', 'door', 'tar', 'top', 'back', 'tale', 'rain', 'tar', 'spell', 'bowl', 'back', 'night', 'bel', 'star', 'guile', 'rain', 'get', 'fin', 'organic', 'land', 'free'] ,'target'))