def crap(a,b,c):
    r=sum(a,[])
    return 'Dog!!' if 'D' in r else ['Cr@p','Clean'][b*c>=r.count('@')]

print(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2))