def invert_hash(d):
    r={}
    for i in d:
        r[d[i]]=i
    return r

print(invert_hash( { 'a' : 1,
    'b' : 2,
    'c' : 3 }))