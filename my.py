def longest_palindrome(s):
    s=s[::-1]
    t='#'.join('^{}$'.format(s))
    n=len(t)
    p=[0]*n
    c=r=0

    for i in range(1,n-1):
        p[i]=(r>i) and min(r-i,p[2*c-i])
        while t[i+1+p[i]]==t[i-1-p[i]]:
            p[i]+=1
        if i+p[i]>r:
            c,r=i,i+p[i]

    m,k=max((n,i) for i,n in enumerate(p))
    return s[(k-m)//2:(k+m)//2]


print(longest_palindrome('jddddjuudjjjdjjjuuudujuudjjjjujdduujduujjujdudjjuuuuuddjjjddddjdj'))
print(longest_palindrome('ttaaftffftfaafatf'))