def pack_basket(w,s):
    a,wt=sorted(map(int,s.replace('dust',' ').split())),[0]*(w+1)
    for i in range(1,len(a)+1):
        for j in range(w,0,-1):
            if a[i-1]<=j:
                wt[j]=max(wt[j],wt[j-a[i-1]]+a[i-1])
    return f'The basket weighs {wt[-1]} kilograms'
    

print(pack_basket(41,'dust 2 7 1 dust 4 75 dust 17 8dust 100dust'))