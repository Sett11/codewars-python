import math as m

def f(n):
    if(n<2):
        return False
    if(n==2):
        return True
    for i in range(2,round(m.sqrt(n))+1):
        if(not n%i):
            return False
    return True

def r(n):
    return max([i if not n%i and f(i) else 0 for i in range(2,round(abs(n)+1))])
        

def ascii_cipher(s,k):
    n=r(k)
    if(k<0):
        n=-n
    s=list(s)
    i=0
    while i<len(s):
        s[i]=(ord(s[i])+n)%128
        if(s[i]<0):
            s[i]+=128
        s[i]=chr(s[i])
        i+=1
    return ''.join(s)

print(ascii_cipher("Encryption rules!", 326))
print(ascii_cipher("Imitation Game, up in here!", -7))
print(ascii_cipher("Hello, world", 18))