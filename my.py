def triple_crown(a):
    r=[]
    [r.append([a[i]['Receiving yards'],a[i]['Receiving touchdowns'],a[i]['Receptions']]) for i in a]
    k=list(zip(*r))
    f=[i for i in a if a[i]['Receiving yards']==max(k[0]) or a[i]['Receiving touchdowns']==max(k[1]) or a[i]['Receptions']==max(k[2])]
    return f[0] if len(f)==1 else 'None of them'

print(triple_crown({'Cooper Kupp': {'Receiving yards': 1700, 'Receiving touchdowns': 18, 'Receptions': 117},
                                         'Justin Jefferson': {'Receiving yards':1650, 'Receiving touchdowns': 17, 'Receptions': 115},
                                        'Davante Adams':{'Receiving yards': 1750, 'Receiving touchdowns': 16, 'Receptions': 113}}))