from re import sub

def cool_string(s):
    c=sub(r'.',lambda e: '1' if e.group().islower() else '2',s)
    return s.isalpha() and '11' not in c and '22' not in c

print(cool_string('aQwFdA'))
print(cool_string('Vvnu'))