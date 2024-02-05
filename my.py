def count_cows(n):
    if isinstance(n,int):
        n+n
        a,c=[0],0
        while n:
            t=0
            for i in range(len(a)):
                a[i]+=1
                if a[i]>=3:
                    t+=1
            a.extend([0]*t)
            c+=t
            n-=1
        return c+1

print(count_cows(2))
print(count_cows(19))