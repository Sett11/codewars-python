def transform(n,b):
    a,r='0123456789abcdef',''
    while n:
        r=a[n%b]+r
        n//=b
    return r

def func(a):
    n=sum(a)//len(a)
    return [n,transform(n,2),transform(n,8),transform(n,16)]


print(func([12,13,6,3,6,45,123]))