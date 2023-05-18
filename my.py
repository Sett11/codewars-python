blz={'R': 1, 'Y': 2, 'G': 3, 'Bn': 4, 'Be': 5, 'P': 6, 'Bk': 7}

import re as r

def frame(b):
    if('W' in b):
        return 'Foul'
    b=[blz.get(i,i) for i in r.sub(r'{}'.format('\d*|'.join(blz.keys())+'\d*'),lambda e:e.group()+' ',b).split(' ') if i]
    i=0
    while i<len(b):
        if(type(b[i])!=int):
            t=r.sub(r'\d+',lambda e:' '+e.group(),b[i]).split(' ')
            b[i]=blz.get(t[0])*int(t[1])
        i+=1
    return sum(b) if sum(b)<148 else 'invalid data'

print(frame('Bk16YGBnBeP'))