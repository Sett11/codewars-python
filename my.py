from itertools import groupby

def consecutive_nums(arr,n):
    arr.sort()
    a=[list(j) for _,j in groupby(arr)]
    while a:
        t=[]
        for i in range(n):
            if i<len(a):
                if not t or a[i][-1]==t[-1]+1:
                    t.append(a[i].pop())
                else:
                    return False
        if len(t)!=n:
            return False
        a=[k for k in a if k]
    return True

print(consecutive_nums([2,3,4,5],2))
print(consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8],3))
print(consecutive_nums([1, 2, 3, 4, 5], 4))