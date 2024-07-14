def solve(arr,k):
    a,n,c=arr.copy(),len(arr),0
    for i in range(n):
        if a[i]=='D':
            for j in range(max(i-k,0),i):
                if a[j]=='C':
                    a[i]=a[j]=0
                    c+=1
                    break
            if a[i]=='D':
                for j in range(i+1,min(i+k+1,n)):
                    if a[j]=='C':
                        a[i]=a[j]=0
                        c+=1
                        break
    return c

print(solve(['C','C','D','D','C','D'],1))