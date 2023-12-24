def f(n):
    a=[1,n]
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            a.extend([i,n//i])
    return len(set(a))
    

a=[(i,f(i)) for i in range(1,20000)]

def count_pairs_int(d,n):
    c=0
    for i in range(n):
        if a[i][1]==a[i+d][1] and a[i+d][0]<n:
            c+=1
    return c

print(count_pairs_int(9,4000))
print(count_pairs_int(1,50))
print(count_pairs_int(7,2500))