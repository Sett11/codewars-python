from collections import Counter


def strings_construction(a,b):
    a,b=Counter(a),Counter([i for i in b if i in a])
    for i in a:
        if i not in b or b[i]<a[i]:
            return 0
        b[i]//=a[i]
    return min(b.values(),default=0)

print(strings_construction('voczsfoppz','ovppppfppsfcsspotczzczfcoofvszapvoc'))