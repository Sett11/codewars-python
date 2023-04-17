def solve(s):
    i=0
    while i<len(s):
        s=s[-1]+s[:-1]
        i+=1
        if(s==s[::-1]):return True
    return False

print(solve('223456776543'))