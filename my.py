from collections import Counter

def last_non_empty_string(s):
    d=Counter(s)
    m=max(d.values())
    return ''.join(sorted(filter(lambda x:d[x]==m,d.keys()),key=lambda y:s.rfind(y)))

print(last_non_empty_string('aabcbbca'))
print(last_non_empty_string('zzxdccvzdd'))
print(last_non_empty_string('abcd'))