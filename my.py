def longest_sequence(n):
    l=r=c=s=1
    while c<=n:
        if s<n:
            r+=1
            c=r**2
            s+=c
        elif s>n:
            s-=l**2
            l+=1
        else:
            return list(range(l,r+1))
    return []


print(longest_sequence(595))