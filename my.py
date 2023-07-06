import re
def debug(s):
    return re.sub(r'bugs|bug',lambda e:e[0] if e[0]=='bugs' else '',s)

print(debug('obugobugobuoobugsoo'))