def count_visible(a):
    m=max(sum(a,()))
    a=[[i+1]+list(j) for i,j in enumerate(a)]
    r=[0]*m
    for i in a:
        r[i[1]-1:i[2]]=[i[0]]*(i[2]-i[1]+1)
    r=set(r)
    l=len(r)
    return l if 0 not in r else l-1

print(count_visible([(564, 566), (923, 927), (668, 674)]))
print(count_visible([(1, 10), (1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))