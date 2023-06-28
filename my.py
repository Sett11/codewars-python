import math
def f(x):
    if x<2:
        return False
    if x==2:
        return True
    for i in range(2,int(math.sqrt(x))+1):
        if not x%i:
            return False
    return True

def circular_prime(n):
    if not f(n):
        return False
    i,s=0,str(n)
    while i<len(s)-1:
        s=s[1:]+s[:1]
        i+=1
        if not f(int(s)):
            return False
    return True

print(circular_prime(9377))