import random

def shuffled_deck():
    a,b,r=['H ', 'C ', 'D ', 'S '],[str(i) for i in[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],[]
    for i in a:
        for j in b:
            r.append(i+j)
    s=[]
    while len(s)<51:
        q=random.randrange(0,52)
        if(q not in s):
            s.append(q)
    i=0
    while i<53:
        if(i not in s):
            s.append(i)
            break
        i+=1
    return [r[i] for i in s]

print(shuffled_deck())