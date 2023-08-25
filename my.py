import re
def drop_cap(s):
    return re.sub(r'([a-z]){3,}',lambda e:e.group().capitalize(),s,flags=re.I)

print(drop_cap('apple of banana'))
print(drop_cap('apple of  banana'))