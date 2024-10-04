from collections import Counter

def odd_one_out(s):
    a=Counter(s)
    return sorted([i for i in a if a[i]&1],key=lambda x:s.rfind(x))

print(odd_one_out('Hello World'))