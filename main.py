from itertools import groupby
from collections import Counter

def same_length(s):
    if s[0] == '0':
        return False
    a, c = [len(list(j)) for i,j in groupby(s)], Counter(s)
    return all(a[i] == a[i+1] for i in range(0, len(a) - 1, 2)) and c['1'] == c['0']

print(same_length('1011100010'))
print(same_length('00110100001111'))