def f(n):
    i,a=2,[]
    while i<=n:
        while n%i==0:
            n//=i
            a.append(i)
        i+=1
    return a

def find_key(k):
    a=f(int(k,16))
    return (a[0]-1)*(a[1]-1)

print(find_key("47b"))
print(find_key("2533"))