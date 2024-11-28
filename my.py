def vowel_recognition(s):
    a,c,b,n=s.lower(),0,'aioue',len(s)
    for i in range(len(a)):
        if a[i] in b:
            c+=(n-i)+(i*(n-i))
    return c

print(vowel_recognition('baceb'))