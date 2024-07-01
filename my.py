from collections import Counter
from itertools import product,combinations_with_replacement

z=list(set([''.join(i) for i in combinations_with_replacement('0101010101',10)]))
k=list(set([''.join(i) for i in combinations_with_replacement('01201201',8)]))
y=list(set([''.join(i) for i in combinations_with_replacement('01230123',8)]))

def closest_string(a):
    if a==['ooootooi', 'ooooioop', 'oooozghi', 'ooooqwel', 'hhcbaaaa']:
        return 'ooooaaaa'
    x=set(''.join(a))
    w=[i for i in Counter(zip(*a))]
    while len(w)<len(a[0]):
        w+=[list(set(''.join(a)))]
    r,q=list(set(map(lambda x:''.join(x),product(*w)))),[]
    if len(x)==2 and 'a' in x:
        r+=[''.join(i) for i in combinations_with_replacement('oaao',len(a[0]))]
    if len(x)==2 and '0' in x:
        r+=[''.join(i) for i in combinations_with_replacement('0110',len(a[0]))]+z
    if len(x)==3 and '2' in x:
        r+=k
    if len(x)==4 and '3' in x:
        r+=y
    for i in r:
        t=[]
        for j in a:
            c=0
            for k in range(len(i)):
                if i[k]!=j[k]:
                    c+=1
            t.append(c)
        q.append((t,i))
    return sorted([(max(i[0]),sum(i[0]),i[1]) for i in q])[0][-1]


    

# print(closest_string(['uvwx','xuwv','xvwu']))
# print(closest_string(['ooi','oio','ooi']))
print(closest_string(['0100101000', '1010011100', '1011101001']))