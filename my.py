def solve(n):
    if n<10:
        return n
    l=len(str(n))
    s='9'*l
    while int(s)>n:
        s=s[1:]
        l-=1
    return 9*len(s)+sum(map(int,str(n-int(s))))

print(solve(7019))