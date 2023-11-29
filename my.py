def longest(s):
    a=[ord(i) for i in s]+[-1]
    o={}
    m=0

    for i in range(len(a)):
        for j in range(i,len(a)-1):
            if a[j]>a[j+1]:
                n=j-i
                m=max(m,n)
                if n not in o:
                    o[n]=s[i:j+1]
                break
    
    return o[m]

print(longest('asdfbyfgiklag'))
print(longest('asdfaaaabbbbcttavvfffffdf'))