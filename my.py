from itertools import permutations as p

def separate(s,a):
    r,x=[],list(s)[::-1]
    for i in a:
        j,t=i,[]
        while j:
            t.append(x.pop())
            j-=1
        r.append(''.join(t))
    return r

comb={3:[[1, 1, 1], [1, 2], [3]],4:[[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2], [4]],5:[[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 4], [2, 3], [5]],6:[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 2], [1, 1, 4], [1, 2, 3], [1, 5], [2, 2, 2], [2, 4], [3, 3], [6]]}

def check(n,k):
    x=str(n*k)
    m=len(x)
    r=[list(x)]
    for i in set(sum([list(p(i)) for i in comb[m][1:-1]],[])):
        r.append(separate(x,i))
    return sum(sum(int(j) for j in i) for i in r)

def next_higher(n,k):
    i=n+1
    while i!=check(i,k):
        i+=1
    return i
    

print(next_higher(2777,4))