def sxore(n):
    if n%2:
        return 0 if n%4==3 else 1
    return n+1 if n%4==2 else n

print(sxore(50))
print(sxore(1000001))