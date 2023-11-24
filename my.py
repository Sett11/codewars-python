def p(n):
    a=[1]
    for i in range(n):
        a.append(a[i]*(n-i)//(i+1))
    return a

def reduce_pyramid(a):
    return sum(x*y for x,y in zip(a,p(len(a)-1)))


print(reduce_pyramid([1,2,3,4]))