from collections import Counter

def find_the_not_fitting_element(a):
    u, c = set(a), Counter(a)
    if len(u) == 2:
        return next(i for i in c if c[i] == 1)
    u, c = set(b:=[type(i) for i in a]), Counter(b)
    if len(u) == 2:
        return next(i for i in a if type(i) == next(j for j in c if c[j] == 1))
    if isinstance(a[0], str) and isinstance(a[-1], str):
        if all(i.isalpha() for i in a):
            u, c = set(b:=[i.islower() for i in a]), Counter(b)
            if len(u) == 2:
                return a[next(i for i, j in enumerate(b) if j)]
        else:
            return next(i for i in a if not i.isalpha())
    if all(i % 2 == 0 for i in a):
        return next(i for i in a if i < 0)
    return next(i for i in a if i & 1)

print(find_the_not_fitting_element(['a', 'a', 'b', 'a', 'a', 'a', 'a']))
print(find_the_not_fitting_element([2, 2, 2, 2, 2, '2']))
print(find_the_not_fitting_element([1, 2, 4, 6, True]))