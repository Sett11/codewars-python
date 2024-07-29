def solve(a,k):
    n,m,r=len(a),0,[]
    for i in range(n):
        c=0
        for j in range(i,n):
            c+=a[j]
            z=j-i+1
            if z>=k:
                y=c/z
                m=max(m,y)
                r.append((y,i,z))
    return sorted([i for i in r if i[0]==m],key=lambda x:(x[-1],x[1]),reverse=True)[0][1:] if r else ()


print(solve([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],3))
print(solve([0],1))