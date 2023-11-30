def longest_substring(s):
    e,o='02468','13579'
    s+='&'
    r={0:''}
    m=i=0

    while i<len(s)-1:
        if (s[i] in e and s[i+1] in e) or (s[i] in o and s[i+1] in o) or s[i+1]=='&':
            t=s[0:i+1]
            n=len(t)
            m=max(m,n)
            if n not in r:
                r[n]=t
            s=s[i+1:]
            i=-1
        i+=1
        
    
    return r[m]


print(longest_substring('225424272163254474441338664823'))
print(longest_substring('594127169973391692147228678476'))