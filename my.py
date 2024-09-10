def check(n):
    s=str(n)
    l=len(s)
    for i in range(1,l+1):
        if int(s[:i])%i:
            return i
    return True

def next_num(n):
    n+=1
    while n<3608528850368400786036726:
        ch=check(n)
        if ch is True:
            return n
        l=len(str(n))
        k=10**(l-ch)
        n=(n//k+1)*k

print(next_num(123220))