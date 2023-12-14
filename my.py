from collections import Counter
from bisect import insort

def original_number(s):
        o=Counter(s.lower())
        d={'w': ('two', '2'), 'u': ('four', '4'), 'x': ('six', '6'), 'f': ('five', '5'), 'z': ('zero', '0'), 'r': ('three', '3'), 't': ('eight', '8'), 's': ('seven', '7'), 'i': ('nine', '9'), 'n': ('one', '1')}
        r=[]
        for i,(j,k) in d.items():
            c=o[i]
            insort(r,k*c)
            for h in j:
                o[h]-=c
        return ''.join(r)


print(original_number('TTONWOHREEE'))