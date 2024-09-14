from collections import Counter

def pos_average(s):
    a,c=[list(i) for i in zip(*s.split(', '))],0
    for i in a:
        for j in Counter(i).values():
            if j>1:
                c+=sum(range(1,j))
    return c/((len(a[0])*(len(a[0])-1)/2)*len(a))*100


print(pos_average("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"))