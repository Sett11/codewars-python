import gmpy2
from bisect import bisect_left,bisect_right

def e(n):
    l=gmpy2.isqrt(n)-1
    n-=1
    b=gmpy2.xmpz(3)
    b[4:n:2]=-1
    for i in b.iter_clear(3,l):
        b[i*i:n:i+i]=-1
    return list(map(lambda x:x**4,b.iter_clear(2,n)))

nums=e(51000)

def solution(n,m):
    return nums[bisect_left(nums,n):bisect_right(nums,m)]

print(solution(10000,100000))