from collections import Counter
from math import gcd

def find_prob(a,b):
    d={'AL': 'Aluminum', 'AM': 'Amber', 'BG': 'Beige', 'BK': 'Black', 'BL': 'Blue', 'BN': 'Brown', 'BZ': 'Bronze', 'CH': 'Charcoal', 'CL': 'Clear', 'GD': 'Gold', 'GN': 'Green', 'GY': 'Gray', 'GT': 'Granite', 'IV': 'Ivory', 'LT': 'Light', 'OL': 'Olive', 'OP': 'Opaque', 'OR': 'Orange', 'PK': 'Pink', 'RD': 'Red', 'SM': 'Smoke', 'TL': 'Translucent', 'TN': 'Tan', 'TP': 'Transparent', 'VT': 'Violet', 'WT': 'White', 'YL': 'Yellow'}
    a,b=Counter(a),[d[i] for i in b]
    total=sum(a.values())
    c=r=1
    for i in b:
        c*=total
        r*=a[i]
        total-=1
        a[i]-=1
    n=gcd(r,c)
    try:
        res=[r//n,c//n]
        return res if all(i for i in res) else ['Impossible']
    except:
        return ['Impossible']

print(find_prob(["Red","Red","Blue","Yellow","Yellow","Yellow","Red", "Yellow","Yellow","Blue","Yellow","Red","Blue","Yellow","Blue","Yellow","Blue","Yellow"],["RD", "YL", "YL", "BL", "GN"]))