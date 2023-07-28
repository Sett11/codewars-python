objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }
objC = { 'a': 5, 'd': 11, 'e': 8 }
objD = { 'c': 3 }

def combine(*a):
    r={}
    for i in a:
        for j in i:
            if r.get(j,'&')=='&':
                r[j]=i[j]
            else:
                r[j]+=i[j]
    return r

print(combine(objA, objB, objC))