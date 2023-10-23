def arbitrate(s,n):
    if '1' not in s:
        return s
    j=s.index('1')
    return ''.join(['0' if i!=j else '1' for i in range(n)])

print(arbitrate('001000101',9))