def rotate_paper(s):
    if any(i in s for i in '1347') or len(s)==1 and s in '69':
        return False
    n=len(s)//2
    for i in range(n):
        if (s[i] in '0258' and s[-i-1]!=s[i]) or (s[i] in '69' and (s[-i-1]==s[i] or s[-i-1] not in '69')):
            return False
    return True


print(rotate_paper('655'))