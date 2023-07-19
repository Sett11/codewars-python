def sakura_fall(v):
    return 80/(v/5) if v>0 else 0

print(sakura_fall(10))
print(sakura_fall(-1))
print(sakura_fall(12.3))