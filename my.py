import re

def baby_count(s):
    s,o,i=list(re.sub(r'[^bay]','',s.lower())),{'a':0,'b':0,'y':0},0
    while i<len(s):
        o[s[i]]+=1
        i+=1
    o['b']//=2
    m=min([i[1] for i in list(o.items())])
    return m if m>=1 else "Where's the baby?!"

print(baby_count('Why the hell are there so many babies?!'))