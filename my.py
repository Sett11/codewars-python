from math import ceil

def graceful_tipping(n):
    k,a,r=n+(n/100*15),[10,100,1000,10000,100000,1000000,10000000],0
    if k<10:
        return ceil(k)
    for i in range(len(a)):
        if k<a[i]:
            r=a[i-1]//2
            break
    for i in range(r,int(k*2),r):
        if i>k:
            return i
    

print(graceful_tipping(739))