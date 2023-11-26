from itertools import permutations

def sc_perm_comb(n):
    s=list(map(int,str(n)))
    r=sum(set(s))

    for i in range(2,len(s)+1):
        r+=sum(set([int(''.join(map(str,j))) for j in permutations(s,i) if j[0]]))

    return r

print(sc_perm_comb(333))
print(sc_perm_comb(190432889))