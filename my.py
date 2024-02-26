def trilingual_democracy(s):
    S='DFKI'
    n=len(set(s))
    if n==1:
        return s[0]
    if n==2:
        return min(((s.count(i),i) for i in s))[1]
    return [i for i in S if i not in s][0]

print(trilingual_democracy("DFF"))