def missing(a,s):
    s=s.replace(' ','')
    try:
        return ''.join(s[i].lower() for i in sorted(a))
    except:
        return "No mission today"

print(missing([0, 3, 5], "I love you"))
print(missing([29, 31, 8], "The quick brown fox jumps over the lazy dog"))