from collections import defaultdict

def min_repeating_character_difference(s):
    if len(s)==len(set(s)):
        return
    a,m=defaultdict(list),float('inf')
    for i in range(len(s)):
        x=s.find(s[i],i+1)
        if x>-1:
            k=x-i
            if k==1:
                return 1,s[i]
            m=min(m,k)
            a[k].append(s[i])
    return m,a[m][0]

print(min_repeating_character_difference('abded'))