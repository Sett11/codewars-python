from re import sub
from collections import Counter

def find_wrong_way_cow(a):
    a=list(map(lambda s:sub(r'[^cow]','.',s),list(map(lambda x:''.join(x),a))))
    z=list(map(lambda s:''.join(s),list(zip(*a))))
    r,q=[],[]
    for i in range(len(a)):
        while 'cow' in a[i] or 'woc' in a[i]:
            if 'cow' in a[i]:
                r.append(['cow',a[i].index('cow'),i])
                a[i]=a[i].replace('cow','aaa',1)
            if 'woc' in a[i]:
                r.append(['woc',a[i].index('woc')+2,i])
                a[i]=a[i].replace('woc','aaa',1)
    for i in range(len(z)):
        while 'cow' in z[i] or 'woc' in z[i]:
            if 'cow' in z[i]:
                q.append(['cow',i,z[i].index('cow')])
                z[i]=z[i].replace('cow','aaa',1)
            if 'woc' in z[i]:
                q.append(['woc',i,z[i].index('woc')+2])
                z[i]=z[i].replace('woc','aaa',1)
    if len(q)==1:
        return [q[0][1],q[0][2]]
    if not q:
        c=Counter([i[0] for i in r])
        w=[j for j in c if c[j]==1][0]
        for i in r:
            if i[0]==w:
                return [i[1],i[2]]
    if len(r)==1:
        return [r[0][1],r[0][2]]
    c=Counter([i[0] for i in q])
    w=[j for j in c if c[j]==1][0]
    for i in q:
        if i[0]==w:
            return [i[1],i[2]]


print(find_wrong_way_cow(['30987 4903247497947947 494797c', '3249874 4978349 (*&(& 9797&(&o', '^^*cowg*9870)*08-090-9-9 --9-w', '*&^*(&^*&(### @@@@@ 2220349409', 'E908E09850 080484844992 293983', '0098 080 KLcowDSFLHU EWPEEJELK', ' dfhdu 880-23fjdlfkjlkjlkjfljf', ';d43-02- -340-2394 39-099kk;ld']))
print(find_wrong_way_cow(list(map(list,"""cccccccccccccccccccccccccccccc
oooooooooooooooooooooooooooooo
wwwwwwwwwwwwwwwwwwwwwwwwwwwwww
cccccccccccccccccccccccccccccc
oooooooooooooooooooooooooooooo
wwwwwwwwwwwwwwwwwwwwwwwwwwwwww
ccccccccccccccwccccccccccccccc
oooooooooooooooooooooooooooooo
wwwwwwwwwwwwwwcwwwwwwwwwwwwwww
cccccccccccccccccccccccccccccc
oooooooooooooooooooooooooooooo
wwwwwwwwwwwwwwwwwwwwwwwwwwwwww
cccccccccccccccccccccccccccccc
oooooooooooooooooooooooooooooo
wwwwwwwwwwwwwwwwwwwwwwwwwwwwww""".split('\n')))))