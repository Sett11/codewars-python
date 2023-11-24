from statistics import mean

def f(n,m):
    a=list(map(int,str(n)))
    return all(sum(a[i:i+4])<=m for i in range(len(a)-3))

def max_sum_dig(n,m):
    a=[i for i in range(1000,n+1) if f(i,m)]
    s,l,c=sum(a),len(a),mean(a)
    r=[]

    for i in range(l):
        if a[i]>c:
            r+=[(c-a[i-1],a[i-1]),(a[i]-c,a[i])]
            break
        
    return [l,sorted(r,key=min)[0][1],s]
    
print(max_sum_dig(82426,9))