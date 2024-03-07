from collections import Counter

def stone_pick(a):
    r=[]
    [r.extend(['Sticks']*4) if x=='Wood' else r.append(x) for x in a if x in ['Cobblestone','Sticks','Wood']]
    d=Counter(r)
    d['Cobblestone']//=3
    d['Sticks']//=2
    return min(d.values())

print(stone_pick(["Wood"]*51 + ["Cobblestone"]*91))