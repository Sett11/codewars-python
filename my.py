def membership(amount, platinum, gold, silver, bronze):
    a,b=[[80, 108, 97, 116, 105, 110, 117, 109],[71, 111, 108, 100],[83, 105, 108, 118, 101, 114],[66, 114, 111, 110, 122, 101]],eval(''.join(map(chr,[97, 109, 111, 117, 110, 116])))
    for i in a:
        s=''.join(map(chr,i))
        if b>=eval(s.lower()):
            return s
    return 'Not a member'

print(membership(100000, 1000000, 100000, 10000, 1000))
print(membership(1001, 1000000, 100000, 10000, 1000))