def build_palindrome(s):
    if s==s[::-1]:
        return s
    for i in range(1,len(s)):
        p=[j for j in [s+s[:i][::-1],s[-i:][::-1]+s] if j==j[::-1]]
        if p:
            return p[0]
        

print(build_palindrome('cdcab'))
print(build_palindrome('abac'))