def f(x):
    if(not '-' in x):
        return [int(x)]
    a,b=[],[]
    [a.append(i) if ':' not in i else a.extend(i.split(':')) for i in x.split('-')]
    a=[int(i) for i in a]
    if(len(a)<3):
        a.append(1)
    return [i for i in range(a[0],a[1]+1,a[2])]

def range_parser(s):
    s,r=[f(i) for i in s.split(',')],[]
    [r.extend(i) for i in s]
    return r

print(range_parser('1-10,14,20-25:2'))