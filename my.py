def size_to_number(s):
    r=''.join(sorted(set(s)))
    if len(r)<3 and not s.endswith('x'):
        if s=='m':
            return 38
        if r=='lx' or s=='l':
            return 40+2*s.count('x')
        if r=='sx' or s=='s':
            return 36-2*s.count('x')


print(size_to_number('xs'))
print(size_to_number('xxxs'))