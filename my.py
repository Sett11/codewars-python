def is_possible(a):
    v,d=True,{}
    def dfs(x,c):
        nonlocal v
        d[x]=c
        for i in a[x]:
            if i not in d:
                dfs(i,0 if c else 1)
            if i in d and d[i]==c:
                v=False
                return
    for i in a:
        if i not in d:
            dfs(i,0)
    return v

print(is_possible({0:[1, 2], 1: [0], 2: [0], 3: [], 4:[5,6], 5:[4], 6:[4]}))
print(is_possible({0:[1, 2,3], 1: [0], 2: [0,3], 3: [2,0]}))
print(is_possible({0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}))