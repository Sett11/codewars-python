def f(x,l='bcdfghjklmnpqrstvwxyz',m='BCDFGHJKLMNPQRSTVWXYZ'):
    if(x in l):return x+'o'+x
    if(x in m):return x+'O'+x
    else:return x
def robber_encode(s):
    return ''.join(map(f,list(s)))

print(robber_encode("S.O.S"))