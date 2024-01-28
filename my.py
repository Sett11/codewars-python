def longest_substring(s):
    c,n=0,len(s)
    for i in range(n):
        z=set()
        for j in range(i,n):
            if s[j] not in z:
                z.add(s[j])
            else:
                break
        c=max(c,len(z))
    return c
    

print(longest_substring("abcd"))
print(longest_substring("hchzvfrkmlnozjk"))
print(longest_substring("abcd" * 10000 + "abcde" + "abcd" * 10000))