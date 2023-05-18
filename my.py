import re as r

def validate_bet(g,t):
    if(r.search(r'[^0-9, ]',t)):
        return None
    t=[int(i) for i in r.split(r' |,',t) if i]
    if(len(t)<g[0] or len(t)>g[1] or len([i for i in t if i>g[1]]) or 0 in t):
        return None
    return sorted(t) if len(set(t))==len(t) and len(t)==g[0] else None

print(validate_bet([5, 71], '8 ,62 ,24 ,19 ,60'))