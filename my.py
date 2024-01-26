def countzero(s):
    a,b=list('abdegopq069DOPQR'),list('%&B8')
    return sum([1 if i in a else 2 if i in b else 0 for i in s])+s.count('()')

print(countzero('abcdefghijklmnopqrstuvwxyz'))