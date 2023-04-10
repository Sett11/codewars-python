def hotpo(n,r=0):
    if(n==1):
        return r
    if(n%2)==0:
        return hotpo(n/2,r+1)
    if(n%2)!=0:
        return hotpo(n*3+1,r+1)

print(hotpo(6))