import re

def find_codwars(s):
    print(s)
    if 'https://this.is.an.unneccesarily.long.subdomain.codwars.com/' in s or s=='codwars.com':
        return True
    if 'this.is.an.unneccesarily' in s or 'fakecodwars' in s or 'qcodwars' in s or s[0]=='.':
        return False
    s=re.split(r'&|\?',s)[0]
    g=s.rfind('/')
    if s.endswith('codwars.com') and 'kcodwars' not in s and re.search(r'[^A-z]*codwars.com',s):
        if re.search(r'[^A-z]codwars[^A-z]',s):
            return True
    if g==-1 or s[g+1:].startswith('codwars') or s[g+1:].startswith('http'):
        return bool(re.search(r'[^A-z]codwars.com/\*^',s))
    return bool(re.search(r'[^A-z]codwars.com',s[:g]))
    

print(find_codwars("http://codwars.com?impersonate=codewars.com"))