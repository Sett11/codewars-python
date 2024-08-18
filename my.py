def find_sequences(n):
    if n==3:
        return [[1, 2]]
    r,q=[sorted(k) for k in [set([j for j in range(n//i-i//2,n//i+i//2+1)]) for i in range(2,int((n**.5)*2))] if all(h>0 for h in k)],[]
    for i in r:
        s=sum(i)
        if s==n:
            q.append(i)
        if s<n:
            x=n-s
            if x==i[0]-1 or x==i[-1]+1:
                q.append(sorted([x]+i))
        if s>n:
            for j in range(1,len(i)):
                if sum(i[:j])==n:
                    q.append(i[:j])
                if sum(i[j:])==n:
                    q.append(i[j:])
    return sorted(map(list,set(map(tuple,q))),reverse=True)
                

print(find_sequences(63))