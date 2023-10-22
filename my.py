def solve(s):
    if s==s[::-1] and len(s)%2==0:
        return False
    s=list(s)
    l=len(s)//2
    for i in range(l+1):
        if s[i]!=s[-i-1] or i==l:
            s[i]=s[-i-1]
            if s==s[::-1]:
                return True
            else:
                return False
    return False

print(solve('abba'))
print(solve('abcba'))