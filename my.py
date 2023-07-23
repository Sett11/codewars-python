def merge_strings(f,s):
    if f==s:
        return f
    i,a=1,[]
    while i<=len(s):
        a.append(s[:i])
        i+=1
    a=sorted([i for i in a if f.endswith(i)],key=lambda e:len(e),reverse=True)
    return f+s if not len(a) else f[:-len(a[0])]+s

print(merge_strings("abcde","cdefgh"))
print(merge_strings('abcde', 'efghi'))
print(merge_strings('abcde', 'bcdefghi'))
print(merge_strings('abaabaab', 'aabaabab'))
print(merge_strings('tedd', 'edd'))