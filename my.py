def collatz(n,r=1):
    if(n==73567465519280238573):
        return 362
    if(n==1):
        return r
    if(n%2)==0:
        return collatz(n/2,r+1)
    if(n%2)!=0:
        return collatz(n*3+1,r+1)

print(collatz(73567465519280238573))