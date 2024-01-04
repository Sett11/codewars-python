from re import sub

def one(a):
    return [''.join([str(j) for j in i]) for i in a]

def two(s):
    return tuple(len(i) for i in sub(r'(.)\1*',lambda x:' '+x.group(),s).split() if i[0]=='1')

def encode(a):
    return tuple(map(two,one(zip(*a)))),tuple(map(two,one(a)))

print(encode((
                        (0, 0, 0, 1, 0, 0, 0, 1, 1, 0),
                        (0, 0, 1, 1, 1, 0, 1, 1, 1, 1),
                        (0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
                        (0, 0, 0, 1, 1, 1, 1, 1, 1, 0),
                        (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
                        (0, 1, 0, 0, 0, 0, 1, 1, 0, 0),
                        (1, 0, 1, 0, 0, 0, 1, 1, 0, 0),
                        (1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
                        (1, 1, 1, 0, 0, 1, 1, 1, 0, 1),
                        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
                      )))