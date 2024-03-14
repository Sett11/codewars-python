from itertools import groupby

def obtain_max_number(a):
    a=[list(j) for i,j in groupby(sorted(a))]
    if all(len(i)==1 for i in a):
        return max(sum(a,[]))
    for i in range(len(a)):
        if len(a[i])==1:
            continue
        else:
            a[i]=a[i][1:]
            a[i][0]*=2
    return obtain_max_number(sum(a,[]))
    

print(obtain_max_number([2, 2, 4, 8, 1, 1, 15]))
print(obtain_max_number([2, 4, 8, 1, 1, 15]))
print(obtain_max_number([2, 4, 8, 1, 1, 32, 8, 8, 64, 30, 30, 15, 15, 7, 7]))