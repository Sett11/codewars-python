def testit(s):
    x,j,r='word',0,''
    a=''.join([i for i in s.lower() if i in x])
    for i in a:
        if i==x[j%4]:
            r+=i
            j+=1
    return r.count(x)

print(testit("When you in order to do something by a wrong way, your heart will missed somewhere."))