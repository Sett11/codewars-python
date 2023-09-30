def closing_in_sum(n):
    s=str(n)
    c=0 if not len(s)&1 else int(s[len(s)//2])
    for i in range(len(s)//2):
        c+=int(s[i]+s[-i-1])
    return c

print(closing_in_sum(1039))
print(closing_in_sum(121))