def strange_math(n,k):
    return sorted(map(str,range(n+1))).index(str(k))

print(strange_math(15,15))