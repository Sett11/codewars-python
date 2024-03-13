from preloaded import A001055

def inf_database(a,s,v):
    d={"equals to":lambda n,k:n==k,"higher than":lambda n,k:n>k,"lower than":lambda n,k:n<k,"higher and equals to":lambda n,k:n>=k,"lower and equals to":lambda n,k:n<=k}
    if s not in d:
        return "wrong constraint"
    r=[i for i in range(a[0],a[1]+1) if d[s](A001055[i],v)]
    return len(r),r