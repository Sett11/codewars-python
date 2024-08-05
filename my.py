def comb(a,r,s):
    n,res=len(a),[]
    t=[0]*r
    def f():
        k=list(a[i] for i in t)
        x=sum(k)
        if x<=s:
            res.append([k,x])
    while 1:
        f()
        for i in reversed(range(r)):
            if t[i]!=i+n-r:
                break
        else:
            return res
        t[i]+=1
        for j in range(i+1,r):
            t[j]=t[j-1]+1

    # w,q=list(set(b)),list(zip(a,b))
    # wc={i:[j[0] for j in q if j[1]==i] for i in w}
    # r=[comb(b,i,n) for i in range(1,len(b))]
    # return r

def pack_bagpack(val,wt,w):
    n,dp=len(val),[0]*(w+1)
    for i in range(1,n+1):
        for j in range(w,0,-1):
            if wt[i-1]<=j:
                dp[j]=max(dp[j],dp[j-wt[i-1]]+val[i-1])
    return dp[w]
    

print(pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10))