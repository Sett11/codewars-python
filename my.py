def manipulate(n):
    s=str(n)
    l=len(s)
    return int(str(s[:l//2]+'0'*(l//2+(1 if l&1 else 0))))

print(manipulate(1234511111))
print(manipulate(123452222))