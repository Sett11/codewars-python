def count_subsequences(t,s):
    n,m=len(s),len(t)
    a=[0]*m
    for i in range(n):
        for j in range(m-1,-1,-1):
            if s[i]==t[j]:
                a[j]+=a[j-1] if j else 1
    return a[-1]

print(count_subsequences("happy birthday", "appyh appy birth day"))
print(count_subsequences("happy birthday", "hhaappyy bbiirrtthhddaayy"))