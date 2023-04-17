import math
def f(x):
    i=1;r=[]
    while i<math.sqrt(x)+1:
        if(x%i==0):
            r.append(i)
            r.append(x/i)
        i+=1
    return sum(set(r))
def r(x,y):
    i=1;m=1
    while i<min(x,y):
        if(x%i==0 and y%i==0):m=max(m,i)
        i+=1
    return m
def friendly_numbers(m,n):
    if(f(n)/n==f(m)/m):return 'Friendly!'
    one=r(f(m),m);two=r(f(n),n)
    return '{0}/{1} {2}/{3}'.format(int(f(m)/one),int(m/one),int(f(n)/two),int(n/two))
    
print(friendly_numbers(10,11))