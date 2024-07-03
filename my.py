def testit(s):
    return ' '.join(map(lambda x:x[::-1].title()[::-1],s.split()))

print(testit('aa bb'))