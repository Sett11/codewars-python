from re import sub

def could_be(o,a):
    f=lambda s:sub(r'[^a-z]','',s)
    o,a=list(map(f,o.replace(':',' ').lower().split())),list(map(f,a.replace(':',' ').lower().split()))
    return bool(a and o) and all(i in o for i in a)

print(could_be('Carlos Ray Norris','Carlos Norris'))