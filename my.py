import re

def double_check(s):
    return True if re.search(r'(.)(\1+)',s,flags=re.I) else False

print(double_check('aabc'))
print(double_check('abcd'))