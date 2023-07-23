import re
def tacofy(w):
    a={'t':'tomato','l':'lettuce','c':'cheese','g':'guacamole','s':'salsa'}
    return ['shell']+[j for j in ['beef' if i in 'aioue' else a.get(i) for i in re.sub(r'.',lambda e:e.group().lower()+' ',w).split(' ') if i] if j]+['shell']

print(tacofy('ogl'))