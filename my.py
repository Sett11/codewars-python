from collections import defaultdict
from itertools import combinations

def check_triangle(x1,y1,x2,y2,x3,y3):
    return 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))

def count_col_triang(a):
    d,r,k=defaultdict(list),{},0
    for i in a:
        d[i[-1]].append(i[0])
    for i in d:
        r[i]=0
        for x,y,z in combinations(d[i],3):
            if check_triangle(*x,*y,*z):
                r[i]+=1
                k+=1
    v=r.values()
    m=max(v)
    return [len(a),len(v),k,sorted(i[0] for i in r.items() if i[1]==m)+[m] if k else []]

print(count_col_triang([[[3, -4], "blue"],  [[-7, -1], "red"], [[7, -6], "yellow"], [[2, 5], "yellow"],
 [[1, -5], "red"], [[-1, 4], "red"], [[1, 7], "red"],[[-3, 5], "red"], [[-3, -5], "blue"], [[4, 1], "blue"] ]))
print(count_col_triang([[[3, -4],
        'blue'], [[-7, -1], 'red'], 
        [[7, -6], 'yellow'], [[2, 5], 'yellow'], 
        [[1, -5], 'red'], [[1, 1], 'red'], 
        [[1, 7], 'red'], [[1, 4], 'red'], 
        [[-3, -5], 'blue'], [[4, 1], 'blue']]))
print(count_col_triang([[[1, -2], 'red'], 
        [[7, -6], 'yellow'], [[2, 5], 'yellow'],
        [[1, -5], 'red'], [[1, 1], 'red'], 
        [[1, 7], 'red'], [[1, 4], 'red'], 
        [[-3, -5], 'blue'], [[4, 1], 'blue']]))