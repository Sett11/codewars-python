from functools import reduce

def colorful(n):
    a,b,i=[int(i) for i in list(str(n))],[],0
    while i<=len(a):
        b.append(a[:i])
        b.append(a[i:])
        j=i+1
        while j<=len(a):
            b.append(a[i:i+j])
            j+=1
        i+=1
    r=[reduce(lambda a,c:int(a)*int(c),i.split(',')) for i in set([','.join([str(j) for j in i]) for i in b if len(i)>1])]+a
    return True if len(set(r))==len(r) else False

print(colorful(263))
print(colorful(236))
print(colorful(235789))
print(colorful(2357893))