def pro_categorization(a, b):
    u, r = sorted(set(sum(b, []))), []
    for i in u:
        t = [[i], []]
        for j in range(len(b)):
            if i in b[j]:
                t[1].append(a[j])
        t[1].sort()
        r.append(t)
    return r

print(pro_categorization(["Jack", "Leon", "Maria"], [
            ["Computer repair", "Handyman", "House cleaning"],
            ["Computer lessons", "Computer repair", "Data recovery service"],
            ["Computer lessons", "House cleaning"]
        ]))