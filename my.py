def maskify(s):
    return '#'*(len(s)-4)+s[-4:]

print(maskify('4556364607935616'))
print(maskify('1'))