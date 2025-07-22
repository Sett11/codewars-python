import re

def regex_contains_all(s):
    return r'^'+r''.join('(?=.*' + i + ')' for i in s)+r'.+$'

s = 'abc'
ss = 'zzzaaacccbbbzzz'

pattern = regex_contains_all(s)

print(re.match(pattern,ss))