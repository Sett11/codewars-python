def count_salutes(s):
    a,b=[],[]
    for i in range(len(s)):
        if s[i]=='<':
            a.append(i)
        elif s[i]=='>':
            b.append(i)
    c=0
    for i in a:
        for j in b:
            if i>j:
                c+=1
    return c*2

print(count_salutes('>--->---<--<'))
print(count_salutes('>-<->-<'))