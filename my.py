def testit(a,b):
    return sorted(list(set(a))+list(set(b)))

print(testit([1,2],[1,2]))