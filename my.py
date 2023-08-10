from itertools import permutations as p
def next_multiple_of_five(n):
    s,c,q='0101',1,bin(n)
    while 1:
        if c>=len(s):
            s+='01'
        t=set([''.join(i) for i in p('0101',c)])
        for i in t:
            x=int(q+i,2)
            if x%5==0:
                return x if n else 5
        c+=1

print(next_multiple_of_five(8516222788))