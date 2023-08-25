def solve(n):
    a=[500,200,100,50,20,10]
    i=c=0
    while n:
        if n<10:
            return -1
        while n>=a[i]:
            n-=a[i]
            c+=1
        i+=1
    return c

print(solve(1500))