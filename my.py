def convert(n,b):
    s='0123456789abcdefghijklmnopqrstuvwxyz'
    r=''
    while n:
        r=s[n%b]+r
        n//=b
    return r

def check(n):
    a=[int(i) for i in str(n)]
    return all(abs(a[i]-a[i+1])==1 for i in range(len(a)-1))

def esthetic(n):
    r=[]
    for i in range(2,11):
        if check(convert(n,i)):
            r.append(i)
    return r

print(esthetic(10))