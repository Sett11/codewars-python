from math import ceil

def cooking_time(n,m,s,p):
    f=float(str(m*60+s))
    a=int(n[:-1])
    b=int(p[:-1])
    c,d=divmod(f/(b/a),60)
    q,w=c,ceil(d)
    if w==60:
        q+=1
        w=0
    return f'{int(q)} minutes {w} seconds'

print(cooking_time("450W", 3, 25, "950W"))
print(cooking_time("600W", 4, 20, "800W"))
print(cooking_time("21W", 64, 88, "25W"))