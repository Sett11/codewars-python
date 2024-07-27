def queue_time(a,n):
    if n==1 or len(a)==1:
        return sum(a)
    if n>=len(a):
        return max(a)
    a=a[::-1]
    t,c=a[-n:],0
    a=a[:-n]
    while a:
        m=min(t)
        for i in range(n):
            t[i]-=m
            if t[i]==0:
                if a:
                    t[i]=a.pop()
                else:
                    break
        c+=m
    return c+max(t)

print(queue_time([3, 9, 3, 9, 11, 47, 38, 47, 42, 46, 30, 33, 31, 1, 11, 24],4))