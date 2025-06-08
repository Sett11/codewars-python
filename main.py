def is_cleanly_nested(a):
    u = set()
    def f(e):
        nonlocal u
        u.add(all(i for i in e) or all(not i for i in e))
        for i in e:
            f(i)
        return
    f(a)
    return (len(u)==1 and u.pop())

print(is_cleanly_nested([]))
print(is_cleanly_nested([[],[]]))
print(is_cleanly_nested([ [ [[]], [[]], [[]]  ], [[]] , [[]]  ]))
print(is_cleanly_nested([ [ [ [[]],[[]], []  ], [[]] ] , [ [] ] ]))