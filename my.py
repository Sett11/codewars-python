def find_dups_miss(a):
    u1,u3,n,m,s=set(),set(),1e10,0,0
    for i in range(len(a)):
        s+=a[i]
        n,m=min(n,a[i]),max(m,a[i])
        if a[i] in u1:
            u3.add(a[i])
            u1.remove(a[i])
        u1.add(a[i])
    return [abs(s-((n+m)*(m-n+1)//2)-sum(u3)),sorted(u3)]
    

print(find_dups_miss([24,25,34,40,38,26,33,29,50,31,33,56,35,36,53,49,57,27,37,40,48,44,32,35,45,52,43,47,26,51,55,28,41,42,46,51,25,30,44,54]))