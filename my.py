def valid(a):
    if not all(len(''.join(i))==len(set(''.join(i))) for i in a) or not all(len(i)==len(a[0]) for i in a) or not all(len(i)==len(a[0][0]) for i in sum(a,[])):
        return False
    d={i:set() for i in ''.join(a[0])}
    try:
        for i in a:
            for j in i:
                for k in j:
                    for c in j.replace(k,''):
                        if c in d[k]:
                            return False
                        else:
                            d[k].add(c)
        return True
    except:
        return False

print(valid( [
  ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
  ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
  ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
  ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
  ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']
 ]))
print(valid([
    ["ABC", "DEF"],
    ["ADE", "CBF"]]))