from itertools import product as p

def possibilities(s):
    n=s.count('?')
    a,r=p('01',repeat=n),[]
    for i in a:
        t=s
        for j in range(len(i)):
            t=t.replace('?',i[j],1)
        r.append(t)
    return r

print(possibilities('1???'))