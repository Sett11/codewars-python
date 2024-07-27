from itertools import product as p

def telephone_words(s):
    d={'1': '1', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ', '0': '0'}
    return [''.join(i) for i in p(*[list(d[j]) for j in s])]

print(telephone_words('1234'))